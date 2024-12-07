#lang racket

(require rackunit)

(define atom?
  (lambda (x)
    (and (not (pair? x)) (not (null? x)))))


(check-false (null? 4))
(check-false (pair? 4))
(check-true (atom? 4))
(check-false (atom? (quote ())))
(check-true (atom? (quote atom)))
(check-true (atom? (quote *abc$)))

(check-true (list? '((a list) is a list)))
(check-eq? (length '((a list) is a list)) 4)
; TODO: Write a length function. You need to define add1
(check-false (atom? '()))
(check-true (list? '()))
(check-true (list? '(() () () ())))


; car or cdr -> what do I get?
(check-equal? (car '(a b c)) 'a)
(check-equal? (car '((a b c) d e)) '(a b c))
(check-equal? (car (car '(((a b c)) d e))) '(a b c))
(check-equal? (cdr '(a b c)) '(b c))
(check-equal? (cdr '(a)) '())
(check-equal? (car (cdr '((b) (x y) ((c))))) '(x y))
(check-equal? (cdr (cdr '((b) (x y) ((c))))) '(((c))))

; List Consing or Creating lists
(check-equal? (cons 'peanut '(butter and jelly)) '(peanut butter and jelly))
(check-equal? (cons '(banana and) '(peanut butter and jelly)) '((banana and) peanut butter and jelly))
(check-equal? (cons '() '()) '(()))
(check-equal? (cons 'a '()) '(a))
(check-equal? (cons '(a) '()) '((a)))
(check-equal? (cons '(a (b)) '()) '((a (b))))
(check-equal? (cons 'a (car '((b) c d))) '(a b))

; Checking list or not
; () is an empty list
(check-true (null? '()))
(check-true (null? (quote ())))
(check-equal? '() (quote ()))
(check-true (atom? (car (cdr '(beef chicken rice fish)))))
(check-true (list? (car (cdr '(beef (chicken hen) rice fish)))))

; Equality Operator
(check-true (eq? 'aynan 'aynan))
(check-false (eq? 'aynan 'fatiha))

;; TODO: List Equality function. The following does not work
;; Primitive eq? works on atoms only.
;;(check-true (eq? '(rice bread) '(rice bread)))
(check-true (eq? 4 4))
(check-false (eq? 4 5))


(define add1
  (lambda x
    (+ (car x) 1)))

;; Chapter 2


;; TODO: Write the function lat?
;; lat? => List of atoms. List cannot have any other list
;; (define (lat? alist)
;;   (cond
;;     ((null? alist))
;;     (else #f)))

(define lat?
  (lambda (alat)
    (cond
      ((null? alat) #t)
      ((atom? (car alat)) (lat? (cdr alat)))
      (else #f))))

;; (check-true (lat? '(a)))
;; (check-true (lat? '()))
;; (check-false (lat? '((a) b)))
;; (list? '(a b c)) -> Is it a list? Yes.
;; (list? '(a b c (d))) -> Is it a list? Yes, too.

(check-true (lat? '()))
(check-true (lat? '(a)))
(check-true (lat? '(a b c)))

;; (check-false (lat? 'a))
(check-false (lat? '((a) b c)))

;; 
;; Note:
;; (cond ...) asks questions
;; (lambda ...) creates a function
;; (define ...) gives it a name











 