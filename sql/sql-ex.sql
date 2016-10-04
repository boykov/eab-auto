mysqladmin -u root -p create ships
mysqladmin -u root -p drop ships
mysql ships < ships_mysql_script.sql
mysql computer < ~/share/computer_mysql_script.sql
mysql ships < query
mysqladmin -u root -p variables 

-- --- 46 --------------------------------------------

SELECT ship, displacement, numGuns
FROM Classes RIGHT JOIN
    Outcomes ON Classes.class = Outcomes.ship
WHERE battle = 'Guadalcanal'
    and outcomes.ship not in
    (select name from ships)
union
SELECT ship, displacement, numGuns
FROM Outcomes  LEFT JOIN
    Ships  ON outcomes.ship = ships.name LEFT JOIN
    Classes  ON ships.class=classes.class
WHERE battle = 'Guadalcanal'
    and outcomes.ship not in (select class from classes)
union
select ship, displacement, numGuns
FROM Classes RIGHT JOIN
    Outcomes ON Classes.class = Outcomes.ship
WHERE battle = 'Guadalcanal'
    and outcomes.ship in
    (select name from ships join classes
	on classes.class=ships.name)

select b.name, c.displacement, c.numGuns
from
    (select s.name, s.class
    from Ships s
    where s.name in (select o.ship from Outcomes o where o.battle='Guadalcanal')
    union
    select c2.class as name, c2.class
    from Classes c2
    where c2.class in
	(select o2.ship
	from Outcomes o2
	where o2.ship not in (select s2.name from Ships s2) and o2.battle='Guadalcanal')) b
    join Classes c on c.class = b.class

SELECT o.ship, c.displacement, c.numGuns
FROM outcomes o left join
    ships s on s.name=o.ship left join
    Classes c on c.class=s.class or o.ship=c.class
where battle='Guadalcanal'

SELECT DISTINCT ship, displacement, numguns
FROM classes
    LEFT JOIN ships ON classes.class=ships.class
    RIGHT JOIN outcomes ON classes.class=ship OR ships.name=ship
WHERE battle='Guadalcanal';
-- ------------------------------------------

-- 1

select Product.type, avg(price) as ap from (
select Product.model, price, Product.type from Product left join PC on Product.model = PC.model
union all
select Product.model, price, Product.type from Product left join Laptop on Product.model = Laptop.model
union all
select Product.model, price, Product.type from Product left join Printer on Product.model = Printer.model
    ) av  right join Product on Product.model = av.model
where Product.model in
(select cc.model from
	(select count(*) num, p1.model from Product p1 join Product p2 on p1.model >= p2.model group by p1.model)
	cc where cc.num % 5 = 0) group by Product.model, Product.type
-- 2

select ship, replace(ship, substring(ship, locate(' ', ship)+1,
	    (length(ship) - locate(' ',reverse(ship))) - locate(' ', ship)),
	repeat('*',(length(ship) - locate(' ',reverse(ship))) - locate(' ', ship))) as rp
from Outcomes where (locate(' ', ship) > 0 and (length(ship ) - locate(' ', reverse(ship)) - locate(' ', ship))>0)


select ship, replace(ship, substring(ship, charindex(' ', ship)+1,
            (len(ship)  - charindex(' ',reverse(ship))) - charindex(' ', ship)),
        replicate('*',(len(ship ) - charindex(' ',reverse(ship))) - charindex(' ', ship)))
from Outcomes where
    (charindex(' ', ship) > 0 and (len(ship ) - charindex(' ', reverse(ship)) - charindex(' ', ship))>0)

select ship, replace(rp, '_', ' ') from
(select ship, concat(substring(shiprp, 1, locate('_', shiprp)) , repeat('*',(length(shiprp) - locate('_',reverse(shiprp))) - locate('_', shiprp))
, substring(shiprp, length(shiprp) - locate('_', reverse(shiprp))+1, locate('_', reverse(shiprp)))) as rp
from (select ship, replace(ship, ' ', '_') as shiprp from Outcomes) bb
where (locate('_', shiprp) > 0 and (length(shiprp) - locate('_', reverse(shiprp)) - locate('_', shiprp))>0)) ff

select ship, replace(rp, '_', ' ') from
(select ship, concat(substring(shiprp, 1, charindex('_', shiprp)) , replicate('*',(datalength(shiprp) - charindex('_',reverse(shiprp))) - charindex('_', shiprp))
, substring(shiprp, datalength(shiprp) - charindex('_', reverse(shiprp))+1, charindex('_', reverse(shiprp)))) as rp
from (select ship, replace(ship, ' ', '_') as shiprp from Outcomes) bb
where (charindex('_', shiprp) > 0 and (datalength(shiprp) - charindex('_', reverse(shiprp)) - charindex('_', shiprp))>0)) ff
