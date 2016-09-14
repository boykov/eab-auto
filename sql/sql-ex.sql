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

-- ------------------------------------------
