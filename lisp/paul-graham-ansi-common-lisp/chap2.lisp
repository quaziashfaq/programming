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
