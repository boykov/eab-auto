(print "test.hy")
(defun test (body)
  (len body))

(defn test2 [lst]
  (len lst))

(defun test3 (body)
  (quasiquote (0 (unquote-splice body))))

(defmacro test4 (body)
  (quasiquote (len (unquote body))))

(print (test [1 2 3 4]))

(print (test2 [1 2 3 4]))

(print (test3 [1 2 3 4]))

(print 1)

(print (test4 [1 2]))
