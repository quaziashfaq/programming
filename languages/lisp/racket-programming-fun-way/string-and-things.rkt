#lang racket

(require rackunit)


(check-equal? (quote (1 (2 3) 4 (5 6))) '(1 (2 3) 4 (5 6)))
(check-equal? (list 1 (list 2 3) 4 (list 5 6)) '(1 (2 3) 4 (5 6)))

(check-equal? (list pi) '(3.141592653589793))
(check-equal? (quote (pi)) '(pi))
(check-equal? (cons 1 (cons 2 (cons 3 4))) '(1 2 3 . 4))
(check-equal? (cdr (cons 1 (cons 2 (cons 3 4)))) '(2 3 . 4))

; '.' is shorthand of 'cons'
(check-equal? '(1 . (2)) '(1 2))

; With 'list' function 'pi' expression is evaluated.
(check-equal? (cons 1 (list pi)) (list 1 pi)) 

; With 'quote' function, 'pi' expression is not evluated
(check-not-equal? (cons 1 (list pi))
                  '(1 pi))


(check-equal? (cons 1 (cons 2 null)) '(1 2)) ; buildig list with cons


;'(1 . 2 . 3)

(check-equal? (cons 'a (cons 'b '())) '(a b))
(check-true (pair? (cons 'a (cons 'b '()))))
(check-equal? '(1 . (2)) '(1 2))

(define (atom? x)
  (and
   (not (pair? x))
   (not (list? x))))


(check-true (atom? "i"))
(check-false (atom? '(1 . 2)))
(check-false (atom? '(1 2)))

(check-eq? (length '(1 2 3)) 3)
(check-equal? (reverse '(1 2 3 4 5)) '(5 4 3 2 1))
(check-equal? (sort '(4 3 5 1 2) < ) '(1 2 3 4 5))
(check-equal? (sort '(4 3 5 1 2) > ) '(5 4 3 2 1))
(check-equal? (append '(1 2 3) '(4 5 6)) '(1 2 3 4 5 6))
(check-equal? (range 0 10 2) '(0 2 4 6 8))
(check-equal? (range 1 11) '(1 2 3 4 5 6 7 8 9 10))
(check-equal? (range 10) '(0 1 2 3 4 5 6 7 8 9))
(check-equal? (make-list 3 'shoma) '(shoma shoma shoma))
(check-true (null? '()))
(check-false (null? '(1 2 3)))
(check-equal? '(list 1 2 3) '(list 1 2 3)) ; ' stops evaluation of expression
(check-equal? (index-of '(8 7 9) 9) 2)
(check-false (index-of '(8 7 9) 10))
(check-equal? (member 7 '(8 7 9)) '(7 9))
(check-false (member 10 '(8 7 9)))


;(define a '(pi 12))
;a
;(set! a 2332)
;a
;(define 2x3 7)
;2x3

(define (ash->imran)
  (display "ash becomes imran\n")
  (display "hello\n"))

;(ash->imran)

(check-equal? (~r pi #:precision 2) "3.14")

(define a '(1 2 3))
(define b '(1 2 3))

(check-true (equal? a b)) ; do they look alike? yes.
(check-false (eq? a b)) ; are they same? no.
(check-true (equal? 12 12))
(check-true (eq? 12 12))
;(= '(1) '(1))
(check-eq? (char->integer #\A) 65)
(check-eq? (char->integer #\u0041) 65)
(check-eq? (integer->char 65) #\A)
(check-true (char-alphabetic? #\u0041))
(check-false (char-alphabetic? #\1))
(check-true (char-numeric? #\1))
(check-false (char-numeric? #\A))

(check-equal? '(#\u2660 #\u2663 #\u2665 #\u2666 #\u0990)
            '(#\♠ #\♣ #\♥ #\♦ #\ঐ))

(check-equal? "happy: \u263a" "happy: ☺")
(check-equal? (string-append "imran" "+" "shoma") "imran+shoma")
(check-eq? (string-ref "abcdef" 2) #\c)

(define what-am-i (string-copy "I am mutable"))
(string-set! what-am-i 5 #\a)
(string-set! what-am-i 6 #\ )
(check-equal? what-am-i "I am a table")
(set! what-am-i (string-append "Human, " what-am-i))

(check-eq? (string-length what-am-i) 19)

(define Xs (make-string 10 #\X))
(check-equal? Xs "XXXXXXXXXX")

(check-equal? (substring what-am-i 9 13) "am a")
(check-equal? (string-titlecase what-am-i) "Human, I Am A Table")
(check-equal? (string-upcase "ash") "ASH")
(check-equal? (string-downcase "ASH") "ash")
(check-true (string<=? "ASH" "ash"))
(check-true (string=? "ash" "ash"))
(check-false (string=? "ash" "ASH"))
(check-equal? (string-replace what-am-i "table" "chair")
              "Human, I am a chair")
(check-true (string-contains? what-am-i "table"))
(check-equal? (string-split what-am-i )
             '("Human," "I" "am" "a" "table"))
(check-equal? (string-split what-am-i ",")
              '("Human" " I am a table"))
(check-equal? (string-trim "  ash   ") "ash")
(check-equal? (string-trim "  ash   " #:right? #f) "ash   ")
(check-equal? (string-trim "  ash   " #:left? #f) "  ash")

(check-equal? (symbol->string 'FBI) "FBI")
(check-equal? (string->symbol "FBI") 'FBI)
(check-equal? (list->string '(#\a #\s #\h)) "ash")
(check-equal? (string->list "ash") '(#\a #\s #\h))
(check-equal? (string->keyword "ash") '#:ash)
(check-equal? (keyword->string '#:ash) "ash")

(check-equal? (format "let ~a = ~a" "x" 2) "let x = 2")
(check-equal? (number->string 10.5) "10.5")
(check-equal? (string->number "10.001") 10.001)


;; VECTOR
(check-equal? (vector 1 2 "a" 'b 3) '#(1 2 "a" b 3))
(check-equal? (vector 1 2 pi) '#(1 2 3.141592653589793))
(check-equal? #(1 2 pi) '#(1 2 pi))