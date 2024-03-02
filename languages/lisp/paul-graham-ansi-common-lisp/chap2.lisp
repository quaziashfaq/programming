; Check if the obj is in the list.
(defun our-member (obj lst)
  (if (null lst)
      nil
      (if (eql (car lst) obj)
          lst
          (our-member obj (cdr lst)))))

(defun ask (string)
  (format t "~A" string)
  (read))

; Read a number
(defun asknumber()
  (format t "Enter an integer: ")
  (let ((val (read)))
    (if (numberp val)
        val
        (asknumber))))

; Print squares of the numbers between start and end (inclusive)
(defun show-squares (start end)
  (do ((i start (+ i 1)))
      ((> i end) 'done)
    (format t "~A ~A ~%" i (* i i))))

; Print cubes of the numbers between start and end (inclusive)
(defun show-cubes (start end)
  (do ((i start (+ i 1)))
      ((> i end) 'done)
    (format t "~A ~A ~%" i (* i i i))))

; Print squares in recursive manner.
(defun show-squares-recursive (i end)
  (if (> i end)
      'done
      (progn
        (format t "~A ~A ~%" i (* i i))
        (show-squares-recursive (+ i 1) end))))

; Measure the length of the list
(defun our-length (lst)
  (let ((len 0))
    (dolist (obj lst)
      (setf len (+ len 1)))
    len))

; Measure the length of the list in recursive way
(defun our-length-recursive (lst)
  (if (null lst)
      0
      (+ (our-length-recursive (cdr lst)) 1 )))
(defun our-fourth (lst)
  (car (cdr (cdr (cdr lst)))))

; Find bigger element of two elements
(defun find-bigger (x y)
  (if (> x y)
      x
      y))

; This function returns for any value of x
(defun enigma (x)
  (and (not (null x))
       (or (null (car x))
           (enigma (cdr x)))))


; Counting the length of objects in y until the object is equal to x
(defun mystery (x y)
  (if (null y)
      nil
      (if (eql (car y) x)
          0
          (let ((z (mystery x (cdr y))))
            (and z (+ z 1))))))

; Find if one of the elements in the list is a list.
(defun find-list (lst)
  (if (null lst)
      nil
      (if (listp (car lst))
      T
      (find-list (cdr lst)))))


(defun print-dots-iterative (n)
  (do ((i 1 (+ i 1)))
      ((> i n) 'done)
    (format t ".")))


(defun print-dots-recursive (n)
  (if (eql n 0)
      'done
      (progn
        (format t ".")
        (print-dots-recursive (- n 1)))))


(defun count-number-of-occurrence-iterative (a lst)
  (let ((n 0))
    (dolist (obj lst)
      (if (eql a obj)
          (setf n (+ n 1))))
    n))

(defun count-number-of-occurrence-recursive (a lst)
  (if (null lst)
      0
      (let ((n 0))
        (if (eql (car lst) a)
            (setf n 1)
            (setf n 0))
        (+ (count-number-of-occurrence-recursive a (cdr lst)) n))))


; Calculate the sum of the elements of the list in iterative way.
(defun summit-i (lst)
  (remove nil lst)
  (let ((n 0))
    (dolist (obj lst)
      (if (numberp obj)
          (setf n (+ n obj))))
    n))


; Calculate the sum of the elements of the list in recursive way.
(defun summit-r (lst)
  (if (null lst)
      0
    (let ((x (car lst)))
      (if (or (null x) (not (numberp x)))
          (+ (summit-r (cdr lst)))
          (+ x (summit-r (cdr lst)))))))

(defun our-listp (x)
  (or (null x) (consp x)))


(defun our-atom (x)
  (not (consp x)))

(defun our-equal (x y)
  (or (eql x y)
      (and (consp x)
           (consp y)
           (our-equal (car x) (car y))
           (our-equal (cdr x) (cdr y)))))


(defun compress (x)
  (if (consp x)
      (compr (car x) 1 (cdr x))
      x))


(defun compr (elt n lst)
  (if (null lst)
      (list (n-elts elt n))
      (let ((next (car lst)))
            (if (eql next elt)
                (compr elt (+ n 1) (cdr lst))
                (cons (n-elts elt n)
                      (compr next 1 (cdr lst)))))))

(defun n-elts (elt n)
  (if (> n 1)
      (list n elt)
      elt))


(defun list-of (n elt)
  (if (zerop n)
      nil
      (cons elt (list-of (- n 1) elt))))

(defun uncompress (lst)
  (if (null lst)
      nil
      (let ((elt (car lst))
            (rest (uncompress (cdr lst))))
        (if (consp elt)
            (append (apply #'list-of elt) ;; Why it works with apply.. But it does not work without apply
                    rest)
            (cons elt rest)))))
