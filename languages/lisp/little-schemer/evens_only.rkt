#lang racket
(require rackunit)

(define atom?
  (lambda (x)
    (and (not (pair? x)) (not (null? x)))))

(define o+
  (lambda (n m)
    (cond
      ((zero? m) n)
      (else (add1 (o+ n (sub1 m)))))))

(check-equal? (o+ 10 2000) 2010)


;; m has to be greater than 0
(define o-
  (lambda (n m)
    (cond
      ((zero? m) n)
      (else (sub1 (o- n (sub1 m)))))))

(check-equal? (o- 10 0) 10)
(check-equal? (o- 10 1) 9)
(check-equal? (o- 10 11) -1)


(define addtup
  (lambda (tup)
    (cond
      ((null? tup) 0)
      (else (o+ (car tup) (addtup (cdr tup)))))))

(check-equal? (addtup '(1 2 3 4 5)) 15)


(define o*
  (lambda (n m)
    (cond
      ((zero? m) 0)
      (else (o+ n (o* n (sub1 m)))))))

(check-equal? (* 4 4) 16)
(check-equal? (o* 4 4) 16)


(define tup+
  (lambda (tup1 tup2)
    (cond
      ;;((and (null? tup1) (null? tup2)) '())
      ((null? tup1) tup2)
      ((null? tup2) tup1)
      (else (cons
             (o+ (car tup1) (car tup2))
             (tup+ (cdr tup1) (cdr tup2)))))))

(check-equal? (tup+ '(1 2 3) '(3 2 1)) '(4 4 4))
(check-equal? (tup+ '(1 2 3 4) '(3 2 1)) '(4 4 4 4))
(check-equal? (tup+ '(1 2 3) '(3 2 1 4)) '(4 4 4 4))

(define o>
  (lambda (n m)
    (cond
      ((and (zero? n) (zero? m)) #f)
      ((zero? n) #f)
      ((zero? m) #t)
      (else (o> (sub1 n) (sub1 m))))))

(check-true (o> 20 10))
(check-false (o> 10 20))
(check-false (o> 10 10))

(define o<
  (lambda (n m)
    (cond
      ((and (zero? n) (zero? m)) #f)
      ((zero? n) #t)
      ((zero? m) #f)
      (else (o< (sub1 n) (sub1 m))))))

(check-false (o< 20 10))
(check-true (o< 10 20))
(check-false (o< 10 10))


(define o=
  (lambda (n m)
    (cond
      ((zero? m) (zero? n))
      ((zero? n) #f)
      (else (o= (sub1 n) (sub1 m))))))

(check-true (o= 0 0))
(check-true (o= 10 10))
(check-false (o= 10 5))
(check-false (o= 5 10))

;; defining expno
(define o^
  (lambda (n m)
    (cond
      ((zero? m) 1)
      (else (o* n (o^ n (sub1 m)))))))

(check-equal? (o^ 2 3) 8)
(check-equal? (o^ 2 3) (expt 2 3))

(define o/
  (lambda (n m)
    (cond
      ((< n m) 0)
      (else (add1 (o/ (o- n m) m))))))

(check-equal? (o/ 10 2) 5)
(check-equal? (o/ 10 3) 3)



(define even?
  (lambda (n)
   (o= (o* (o/ n 2) 2) n)))


(check-true (even? 10))
(check-false (even? 11))


(define evens-only*
  (lambda (l)
    (cond
      ((null? l) '())
      ((atom? (car l))
       (cond
         ((even? (car l)) (cons (car l) (evens-only* (cdr l))))
         (else (evens-only* (cdr l)))))
      (else (cons (evens-only* (car l)) (evens-only* (cdr l)))))))


(evens-only* '((1 2 11 20) 14 15 16 (17 18 19 20)))
