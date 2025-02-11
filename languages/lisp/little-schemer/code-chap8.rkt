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

;; DONE: Write a length function. You need to define add1
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

;; Equality Operator
(check-true (eq? 'blueberry 'blueberry))
(check-false (eq? 'blueberry 'fatiha))

;; TODO: List Equality function. The following does not work
;; Primitive eq? works on atoms only.
;; (check-true (eq? '(rice bread) '(rice bread)))
(check-true (eq? 4 4))
(check-false (eq? 4 5))


;; add1 is primitive function. No need to define it actually?
;; 
;; (define add1
;;   (lambda (x)
;;     (+ x 1)))




;;--------------------------------------------------------
;; Chapter 2 : Do it, Do It Again, and Again, and Again...
;;--------------------------------------------------------

;; Definition of lat? function
;; lat? means is it a list of (only) atoms.
(define lat?
  (lambda (alat) ;; alat = a list of atoms
    (cond
      ((null? alat) #t)
      ((atom? (car alat)) (lat? (cdr alat)))
      (else #f))))

;; The empty list is also a list of atoms
(check-true (lat? '()))

(check-true (lat? '(a)))
(check-true (lat? '(a b c)))
(check-true (list? '(a b c)))

;; '((a) b c)) is a list but not a list of atoms.
(check-false (lat? '((a) b c)))
(check-true (list? '((a) b c)))

;; 
;; Note:
;; (define ...) gives it a name
;; (lambda ...) creates a function
;; (cond ...) asks questions

;; This is my definition of length of a list
;; The actual function name is length
(define ash-length
  (lambda (alist)
    (cond
      ((null? alist) 0)
      (else (add1 (ash-length (cdr alist)))))))
      

(check-equal? (add1 10) 11)
(check-equal? (ash-length '(a b c d)) 4)
(check-equal? (ash-length '(a (b c) d)) 3)

(check-equal? (length '(a b c d)) 4)

;; This is my definition to find if an atom is a member of a list of atoms
;; The actual functino name is member?
;; (define little-schemer-member?
;;   (lambda (x alat) ;; test
;;     ;;(print alat)
;;     (cond
;;       ((null? alat) #f)
;;       ((eq? x (car alat)) #t)
;;       (else (little-schemer-member? x (cdr alat))))))
;; 
;; The actual 'member' function in racket does the below:
;; Returns the whole list if the atom is the member of the list
;; (member 'a '(a b)) => '(a b)
;; Returns false if the atom is not a member of the list.
;; (member 'c '(a b)) => #f
   
;; (check-true (little-schemer-member? 'a '(a b c d)))
;; (check-true (little-schemer-member? 'b '(a b c d)))
;; (check-true (little-schemer-member? 'c '(a b c d)))
;; (check-true (little-schemer-member? 'd '(a b c d)))
;; (check-false (little-schemer-member? 'e '(a b c d)))
;; (check-false (little-schemer-member? 'a '()))

(define o=
  (lambda (n m)
    (cond
      ((zero? m) (zero? n))
      ((zero? n) #f)
      (else (o= (sub1 n) (sub1 m))))))

;; Are two atoms or numbers equal?
(define eqan?
  (lambda (a1 a2)
    (cond
      ((and (number? a1) (number? a2)) (o= a1 a2))
      ((or (number? a1) (number? a2)) #f)
      (else (eq? a1 a2)))))

(check-true (eqan? 10 10))
(check-false (eqan? 10 9))
(check-false (eqan? 10 'blueberry))
(check-false (eqan? 'dragonfruit 'blueberry))
(check-true (eqan? 'blueberry 'blueberry))

(define eqlist?
  (lambda (l1 l2)
    (cond
      ((and (null? l1) (null? l2)) #t)
      ((or (null? l1) (null? l2) #f))
      (else (and (little-schemer-equal? (car l1) (car l2))
                 (eqlist? (cdr l1) (cdr l2)))))))

(define little-schemer-equal?
  (lambda (s1 s2)
    (cond
      ((and (atom? s1) (atom? s2)) (eqan? s1 s2))
      ((or  (atom? s1) (atom? s2)) #f)
      (else (eqlist? s1 s2)))))

(check-true (little-schemer-equal? 'potato 'potato))
(check-true (little-schemer-equal? '(potato) '(potato)))

(check-true (eqlist? '(straberry ice cream)
                     '(straberry ice cream)))

(check-true (eqlist? 
'(((tomato vorta sauce)) ((bean) vorta sauce) (and ((flying)) vorta sauce))
'(((tomato vorta sauce)) ((bean) vorta sauce) (and ((flying)) vorta sauce))))

(check-false (eqlist? 
'(((tomato vorta sauce)) ((bean) vorta sauce) (and ((flying)) vorta sauce))
'(((tomato vorta sauce)) ((bean) vorta sauce) (and ((flying)) vorta (sauce)))))

;; Redefining the little-schemer-member? function here
(define member?
  (lambda (x alat)
    (cond
      ((null? alat) #f)
      ((little-schemer-equal? x (car alat)) #t)
      (else (member? x (cdr alat))))))

(check-true (member? 'a '(a b c d)))
(check-true (member? 'b '(a b c d)))
(check-true (member? 'c '(a b c d)))
(check-true (member? 'd '(a b c d)))
(check-false (member? 'e '(a b c d)))
(check-false (member? 'a '()))


 
;; The definition of member?
;; as per the book 'The Little Schemer.
;; a bit of improvement with 'or' function.
;; (define member?
;;   (lambda (x alat)
;;     ;;(print alat)
;;     (cond
;;       ((null? alat) #f)
;;       (else (or (eq? x (car alat))
;;                 (member? x (cdr alat)))))))
;; 
;; 
;; (check-true (member? 'a '(a b c d)))
;; (check-true (member? 'b '(a b c d)))
;; (check-true (member? 'c '(a b c d)))
;; (check-true (member? 'd '(a b c d)))
;; (check-false (member? 'e '(a b c d)))
;; (check-false (member? 'a '()))
;; 

;;--------------------------------------------------------
;; Chapter 3 : Cons the Magnificent
;;--------------------------------------------------------

;; Function to remove a member of a list of atoms
;; Remove the first occurrence
;; (define rember
;;   (lambda (x alat)
;;     (cond
;;       ((null? alat) '())
;;       ((eq? x (car alat)) (cdr alat))
;;       (else (cons (car alat) (rember x (cdr alat)))))))


;; (define rember
;;   (lambda (s l)
;;     (cond
;;       ((null? l) '())
;;       ((eq? s (car l)) (cdr l))
;;       (else (cons (car l) (rember s (cdr l)))))))
;; 



;; From the list of list of atoms/lists, get the first item of each of the list.
(define firsts
  (lambda (lol) ;; lol = list of lists
    (cond
      ((null? lol) '())
      (else (cons (car (car lol))
                  (firsts (cdr lol)))))))

;; (firsts
;;  '((apple peach pumpkin)
;;    (plum pear cherry)
;;    (grape raisin pea)
;;    (bean carrot epgplant)))


(check-equal?
 (firsts
 '((apple peach pumpkin)
   (plum pear cherry)
   (grape raisin pea)
   (bean carrot epgplant)))
 '(apple plum grape bean))

(check-equal?
 (firsts
  '(((five plums) four)
    (eleven green oranges)
    ((no) more)))
 '((five plums) eleven (no)))

(check-equal? (first '(a b c)) 'a)

;; Substitute the first occurrence of old1 or old2 item with the
;; new item in the list.
(define subst2
  (lambda (new old1 old2 lat)
    (cond
      ((null? lat) '())
      ((or (eq? (car lat) old1)
           (eq? (car lat) old2))
       (cons new (cdr lat)))
      (else (cons (car lat) (subst2 new old1 old2 (cdr lat)))))))


;;(insertL 'topping 'fudge '(ice cream with fudge for dessert))

(check-equal? (subst2 'vanilla 'chocolate 'banana '(banana ice cream with chocolate topping))
              '(vanilla ice cream with chocolate topping))
(check-equal? (subst2 'vanilla 'chocolate 'banana '(chocolate ice cream with banana topping))
              '(vanilla ice cream with banana topping))
(check-equal? (subst2 'vanilla 'banana 'chocolate '(banana ice cream with chocolate topping))
              '(vanilla ice cream with chocolate topping))


;; Remove all the occurrences of an item from the list.
(define multirember
  (lambda (x alat)
    (cond
      ((null? alat) '())
      ;; ((eq? x (car alat)) (multirember x (cdr alat)))
      ;; Replacing eq? with little-schemer-equal? function
      ((little-schemer-equal? x (car alat)) (multirember x (cdr alat)))
      (else (cons (car alat) (multirember x (cdr alat)))))))

(check-equal? (multirember 'a '(a b a b c d a)) '(b b c d))
(check-equal? (multirember '(a b) '((a b) a b c d (a b))) '(a b c d))


;; Insert a new item after all the occurrences of an item (old) in the list
(define multiinsertR
  (lambda (new old lat)
    (cond
      ((null? lat) '())
      ((eq? (car lat) old) (cons old (cons new (multiinsertR new old (cdr lat)))))
      (else (cons (car lat) (multiinsertR new old (cdr lat)))))))


(check-equal? (multiinsertR 'a 'b '(b b c d)) '(b a b a c d))


;; Insert a new item before all the occurrences of an item (old) in the list
(define multiinsertL
  (lambda (new old lat)
    (cond
      ((null? lat) '())
      ((eq? (car lat) old) (cons new (cons old (multiinsertL new old (cdr lat)))))
      (else (cons (car lat) (multiinsertL new old (cdr lat)))))))

(check-equal? (multiinsertL 'a 'b '(b b c d)) '(a b a b c d))


;; Substitune all the occurrences of an old item in the list with the new item.
(define multisubst
  (lambda (new old lat)
    (cond
      ((null? lat) '())
      ((eq? (car lat) old) (cons new (multisubst new old (cdr lat))))
      (else (cons (car lat) (multisubst new old (cdr lat)))))))

(check-equal? (multisubst 'topping 'fudge '(ice cream with fudge for dessert fudge))
              '(ice cream with topping for dessert topping))




;;--------------------------------------------------------
;; Chapter 4 : Numbers Games
;;--------------------------------------------------------
(check-true (atom? 14))
(check-equal? (add1 10) 11)

;; sub1 is a primitive function. No need to define it by me.
;; (define sub1
;;   (lambda (n)
;;     (- n 1)))

(check-equal? (sub1 0) -1)


;; zero? is a primivet function. No need to define.
;; (define zero?
;;   (lambda (n)
;;     (= n 0)))

(check-true (zero? (sub1 1)))

;; m has to be greater than 0
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


;; 'length' is already defined in racket
;; I have defined as ash-length earlier.


;; (pick n lat)
;; n > 0
;; n >= (length lat) > 0
(define pick
  (lambda (n lat)
    (cond
      ((zero? (sub1 n)) (car lat))
      (else (pick (sub1 n) (cdr lat))))))

(check-equal? (pick 1 '(lasagna spaghetti raviolli macaroni meatball)) 'lasagna)
(check-equal? (pick 4 '(lasagna spaghetti raviolli macaroni meatball)) 'macaroni)



;; (rempick n lat) => pick and remove an item from the lat.
;; n > 0
;; n >= (length lat) > 0

(define one?
  (lambda (n)
    (o= n 1)))

(check-true (one? 1))
(check-false (one? 2))

(define rempick
  (lambda (n lat)
    (cond
      ;;((zero? (sub1 n)) (cdr lat))
      ((one? n) (cdr lat))
      (else (cons (car lat)
                  (rempick (sub1 n) (cdr lat)))))))


(check-equal? (rempick 1 '(lasagna spaghetti raviolli macaroni meatball))
              '(spaghetti raviolli macaroni meatball))
(check-equal? (rempick 4 '(lasagna spaghetti raviolli macaroni meatball))
              '(lasagna spaghetti raviolli meatball))


;; remove all the numbers from the list of atoms.
(define no-nums
  (lambda (lat)
    (cond
      ((null? lat) '())
      ((number? (car lat)) (no-nums (cdr lat)))
      (else (cons (car lat) (no-nums (cdr lat)))))))

(check-equal? (no-nums '(5 mangoes 6 bananas 7 dates)) '(mangoes bananas dates))


;; remove the non-numbers from the list of atoms.
(define all-nums
  (lambda (lat)
    (cond
      ((null? lat) '())
      ((number? (car lat)) (cons (car lat) (all-nums (cdr lat))))
      (else (all-nums (cdr lat))))))

(check-equal? (all-nums '(5 mangoes 6 bananas 7 dates)) '(5 6 7))



(define occur
  (lambda (a lat)
    (cond
      ((null? lat) 0)
      ((eqan? a (car lat)) (add1 (occur a (cdr lat))))
      (else (occur a (cdr lat))))))

(check-equal? (occur 5 '(5 mangoes 5 bananas 5 dates)) 3)



;;--------------------------------------------------------
;; Chapter 5 : *Oh My Gawd*: It's Full of Stars
;;--------------------------------------------------------

(define rember*
  (lambda (a l)
    (cond
      ((null? l) '())
      ((atom? (car l)) (cond
                         ((eqan? a (car l)) (rember* a (cdr l)))
                         (else (cons (car l) (rember* a (cdr l))))))
      (else (cons (rember* a (car l)) (rember* a (cdr l)))))))

(check-equal? (rember* 5 '(5 mangoes 5 bananas 5 dates)) '(mangoes bananas dates))
(check-equal? (rember* 'sauce '(((tomato sauce))
                               ((bean) sauce)
                               (and ((flying)) sauce)))
              '(((tomato)) ((bean)) (and ((flying)))))


;; The First Commandment

;; When recurring on a list of atoms, lat,
;; ask two questions about it: (null? lat) and
;; else recurn on (cdr lat)

;; When recurring on a number, n > 0,
;; ask two questions about it: (zero? n) and
;; else recur on (sub1 n)

;; When recurring on a list of S-expressions, l,
;; ask three questions about it: (null? l), (atom? (car l)) and
;; else recurn on (car l) and (cdr l) if neither (null? l) and (atom? (car l)) are true





(define insertR*
  (lambda (new old l)
    (cond
      ((null? l) '())
      ((atom? (car l)) (cond
                         ((eqan? old (car l)) (cons old (cons new (insertR* new old (cdr l)))))
                         (else (cons (car l) (insertR* new old (cdr l))))))
      (else (cons (insertR* new old (car l))
                  (insertR* new old (cdr l)))))))

(check-equal? (insertR* 'vorta 'sauce
                       '(((tomato sauce))
                         ((bean) sauce)
                         (and ((flying)) sauce)))
              '(((tomato sauce vorta))
                ((bean) sauce vorta)
                (and ((flying)) sauce vorta)))



(check-equal?
 (insertR* 'roast 'chuck '((how much (wood)) could ((a (wood) chuck)) (((chuck))) (if (a) ((wood chuck))) could chuck wood))
 '((how much (wood)) could ((a (wood) chuck roast)) (((chuck roast))) (if (a) ((wood chuck roast))) could chuck roast wood))



;; How many times an atom is found in l
(define occur*
  (lambda (a l)
    (cond
      ((null? l) 0)
      ((atom? (car l)) (cond
                         ((eqan? a (car l)) (add1 (occur* a (cdr l))))
                         (else (occur* a (cdr l)))))
      (else (o+ (occur* a (car l)) (occur* a (cdr l)))))))

(check-equal? 5 (occur* 'banana
                        '((banana) (split ((((banana ice)))
                                           (cream (banana))
                                           sherbet))
                                   (banana) (bread) (banana brandy))))


(define subst*
  (lambda (new old l)
    (cond
      ((null? l) '())
      ((atom? (car l)) (cond
                         ((eqan? old (car l)) (cons new (subst* new old (cdr l))))
                         (else (cons (car l) (subst* new old (cdr l))))))
      (else (cons (subst* new old (car l))
                  (subst* new old (cdr l)))))))

(check-equal? (subst* 'vorta 'sauce
                       '(((tomato sauce))
                         ((bean) sauce)
                         (and ((flying)) sauce)))
              '(((tomato vorta))
                ((bean) vorta)
                (and ((flying)) vorta)))



(define insertL*
  (lambda (new old l)
    (cond
      ((null? l) '())
      ((atom? (car l)) (cond
                         ((eqan? old (car l)) (cons new (cons old (insertL* new old (cdr l)))))
                         (else (cons (car l) (insertL* new old (cdr l))))))
      (else (cons (insertL* new old (car l))
                  (insertL* new old (cdr l)))))))

(check-equal? (insertL* 'vorta 'sauce
                       '(((tomato sauce))
                         ((bean) sauce)
                         (and ((flying)) sauce)))
              '(((tomato vorta sauce))
                ((bean) vorta sauce)
                (and ((flying)) vorta sauce)))


(define member*
  (lambda (a l)
;;    (display l)
;;    (display "\n")
    (cond
      ((null? l) #f)
      ((atom? (car l))(cond
                        ((eqan? a (car l)) #t)
                        (else (member* a (cdr l)))))
      (else (or (member* a (car l)) (member* a (cdr l)))))))

          
(check-true (member* 'chips '((potatto) (chips ((with) fish) (chips)))))
(check-true (member* 'sauce '(((tomato vorta sauce)) ((bean) vorta sauce) (and ((flying)) vorta sauce))))
(check-false (member* 'meat '((potatto) (chips ((with) fish) (chips)))))


(define leftmost
  (lambda (l)
    (cond
      ((null? l) '())
      ((atom? (car l)) (car l))
      (else (leftmost (car l))))))

(check-equal? 'potato (leftmost '((potato) (chips ((with) fish) (chips)))))
(check-equal? 'tomato (leftmost '(((tomato vorta sauce)) ((bean) vorta sauce) (and ((flying)) vorta sauce))))



;; (define asheqlist?
;;   (lambda (l1 l2)
;;     (cond
;;       ((and (null? l1) (null? l2)) #t)
;;       ((or (null? l1) (null? l2) #f))
;;       ((and (atom? (car l1)) (atom? (car l2)))
;;        (and (eqan? (car l1) (car l2)) (eqlist? (cdr l1) (cdr l2))))
;;       ((and (list? (car l1)) (list? (car l2))) (and
;;                                                 (eqlist? (car l1) (car l2))
;;                                                 (eqlist? (cdr l1) (cdr l2))))
;;       (else #f))))

;; (define eqlist?
;;   (lambda (l1 l2)
;;     (cond
;;       ((and (null? l1) (null? l2)) #t)
;;       ((or (null? l1) (null? l2) #f))
;;       ((and (atom? (car l1)) (atom? (car l2)))
;;        (and (eqan? (car l1) (car l2)) (eqlist? (cdr l1) (cdr l2))))
;;       ((or (atom? (car l1)) (atom? (car l2))) #f)
;;       (else (and (eqlist? (car l1) (car l2))
;;                  (eqlist? (cdr l1) (cdr l2)))))))










;;--------------------------------------------------------
;; Chapter 6 : Shadows
;;--------------------------------------------------------

(define numbered?
  (lambda (aexp)
    (cond
      ((atom? aexp) (number? aexp))
      (else (and
             (numbered? (car aexp))
             (numbered? (car (cdr (cdr aexp)))))))))

(check-true (numbered? 3))
(check-true (numbered? '(3 + 4)))
(check-true (numbered? '((1 + 2) + (2 * 2))))

;; The function has bugs. I can put anything in the place of operators.
(check-true (numbered? '((1 + 2) a (2 * 2))))

;; Checking the value of (a + b)
;; (define value
;;   (lambda (nexp)
;;     (cond
;;       ((atom? nexp) nexp)
;;       (else (cond
;;               ((eq? (car (cdr nexp)) '^) (o^ (value (car nexp)) (value (car (cdr (cdr nexp))))))
;;               ((eq? (car (cdr nexp)) '*) (o* (value (car nexp)) (value (car (cdr (cdr nexp))))))
;;               ((eq? (car (cdr nexp)) '+) (o+ (value (car nexp)) (value (car (cdr (cdr nexp)))))))))))
;; 
;; (value 5)
;; (value '(5 + 5))
;; (value '((5 * 2) ^ (3 + 1)))

;; Finding the value of (+ a b)
;; (define value
;;   (lambda (nexp)
;;     (cond
;;       ((atom? nexp) nexp)
;;       (else (cond
;;               ((eq? (car nexp) '^) (o^ (value (car (cdr nexp))) (value (car (cdr (cdr nexp))))))
;;               ((eq? (car nexp) '*) (o* (value (car (cdr nexp))) (value (car (cdr (cdr nexp))))))
;;               ((eq? (car nexp) '+) (o+ (value (car (cdr nexp))) (value (car (cdr (cdr nexp)))))))))))
;; 

;; (value 5)
;; (value '(+ 5 5))
;; (value '(^ (* 5 2) (+ 3 1)))


(define 1st-sub-exp
  (lambda (aexp)
    (car (cdr aexp))))

(define 2nd-sub-exp
  (lambda (aexp)
    (car (cdr (cdr aexp)))))

(define operator
  (lambda (aexp)
    (car aexp)))

;; (define value
;;   (lambda (nexp)
;;     (cond
;;       ((atom? nexp) nexp)
;;       (else (cond
;;               ((eq? (operator nexp) '^) (o^ (value (1st-sub-exp nexp)) (value (2nd-sub-exp nexp))))
;;               ((eq? (operator nexp) '*) (o* (value (1st-sub-exp nexp)) (value (2nd-sub-exp nexp))))
;;               ((eq? (operator nexp) '+) (o+ (value (1st-sub-exp nexp)) (value (2nd-sub-exp nexp)))))))))

(define atom-to-function
  (lambda (x)
    (cond
      ((eq? x (quote ^)) o^)
      ((eq? x (quote *)) o*)
      ((eq? x (quote +)) o+))))

(define value
  (lambda (nexp)
    (cond
      ((atom? nexp) nexp)
      (else ((atom-to-function (operator nexp)) (value (1st-sub-exp nexp)) (value (2nd-sub-exp nexp)))))))


(check-equal? ((atom-to-function (operator '(* 10 11))) 5 6) 30)
(check-equal? (value 5) 5)
(check-equal? (value '(+ 5 5)) 10)
(check-equal? (value '(^ (* 5 2) (+ 3 1))) 10000)



(define sero?
  (lambda (n)
    (null? n)))

(check-true (sero? '()))
(check-false (sero? '(())))

(define edd1
  (lambda (n)
    (cons '() n)))

(check-equal? '(() ()) (edd1 '(())))

(define zub1
  (lambda (n)
    (cdr n)))

(check-equal? '(() ()) (zub1 '(() () ())))



;;--------------------------------------------------------
;; Chapter 7 : Friends and Relations
;;--------------------------------------------------------

;; Set? is this a set?
;; (define set?
;;   (lambda (lat)
;;     (cond
;;       ((null? lat) #t)
;;       ((o> (occur (car lat) lat) 1) #f)
;;       (else (set? (cdr lat))))))
;; 

(define set? 
  (lambda (lat)
    (cond
      ((null? lat) #t)
      ((member? (car lat) (cdr lat)) #f)
      (else (set? (cdr lat))))))


(check-false (set? '(apple mango banana apple)))
(check-false (set? '(mango banana apple apple)))
(check-true (set? '(mango banana apple orange)))
(check-false (set? '(apple 3 pear 4 9 apple 3 4)))

(define makeset
  (lambda (lat)
    (cond
      ((null? lat) '())
      ((member? (car lat) (cdr lat)) (cons (car lat) (makeset (multirember (car lat) (cdr lat)))))
      (else (cons (car lat) (makeset (cdr lat)))))))

(check-equal? (makeset '(apple peach pear peach plum apple lemon peach)) '(apple peach pear plum lemon))
(check-equal? (makeset '(5 apple peach 5 pear 5 peach plum apple 5 lemon peach)) '(5 apple peach pear plum lemon))


(define ls-subset?
  (lambda (s1 s2)
    (cond
      ((null? s1) #t)
      (else (and (member? (car s1) s2)
                 (ls-subset? (cdr s1) s2))))))

(check-true (ls-subset? '() '()))
(check-true (ls-subset? '() '(a b)))
(check-true (ls-subset? '(a) '(a b)))
(check-true (ls-subset? '(a b) '(a b)))
(check-false (ls-subset? '(a b c) '(a b)))

(define eqset?
  (lambda (s1 s2)
    (and (ls-subset? s1 s2) (ls-subset? s2 s1))))

(check-true (eqset? '(a b c) '(c a b)))

(define intersect? 
  (lambda (s1 s2)
    (cond
      ((null? s1) #f)
      (else (or (member? (car s1) s2) (intersect? (cdr s1) s2))))))

(check-true (intersect? '(blueberry orange watermelon) '(strawberry guava watermelon mango)))
(check-false (intersect? '(blueberry orange watermelon) '(strawberry guava mango)))

(define intersect
  (lambda (s1 s2)
;;     (display "In intersect: ") (display s1) (display s2) (newline)
    (cond
      ((null? s1) '())
      ((member? (car s1) s2) (cons (car s1) (intersect (cdr s1) s2)))
      (else (intersect (cdr s1) s2)))))


(check-equal? (intersect '(blueberry orange watermelon) '(strawberry guava watermelon mango)) '(watermelon))


(define union
  (lambda (s1 s2)
    (cond
      ((null? s1) s2)
      ((member? (car s1) s2) (union (cdr s1) s2))
      (else (cons (car s1) (union (cdr s1) s2))))))

(check-equal? (union '(blueberry orange watermelon) '(strawberry guava watermelon mango))
              '(blueberry orange strawberry guava watermelon mango))
(check-equal? (union '() '()) '())
(check-equal? (union '(blueberry) '()) '(blueberry))
(check-equal? (union '() '(watermelon)) '(watermelon))
(check-equal? (union '(orange) '(watermelon)) '(orange watermelon))

(define difference
  (lambda (s1 s2)
    (cond
      ((null? s1) '())
      ((member? (car s1) s2) (difference (cdr s1) s2))
      (else (cons (car s1) (difference (cdr s1) s2))))))



(check-equal? (difference '(blueberry orange watermelon) '(strawberry guava watermelon mango)) '(blueberry orange))
(check-equal? (difference '(blueberry orange watermelon) '(strawberry guava watermelon mango blueberry orange)) '())


(define intersectall
  (lambda (l-set)
;;     (display l-set) (newline)
    (cond
;;       ((null? l-set) '())
      ((null? (cdr l-set)) (car l-set))
      (else
;;        (display (car l-set)) (newline)
;;        (display (cdr l-set)) (newline)
       (intersect (car l-set) (intersectall (cdr l-set)))))))

(check-equal? (intersectall '((a b c) (c a d e) (e f g h a b))) '(a))


;; pair?
;;
(define a-pair?
  (lambda (x)
    (cond
      ((atom? x) #f)
      ((null? x) #f)
      ((null? (cdr x)) #f)
      ((null? (cdr (cdr x))) #t)
      (else #f))))

(check-true (a-pair? '(bread butter)))
(check-true (a-pair? '((bread) butter)))
(check-true (a-pair? '(bread (butter))))
(check-true (a-pair? '((bread) (butter))))
(check-true (a-pair? '(bread (butter))))

(define pfirst
  (lambda (p)
    (car p)))

(define psecond
  (lambda (p)
    (car (cdr p))))

(check-equal? (pfirst '(bread butter)) 'bread)
(check-equal? (psecond '(bread butter)) 'butter)

(define build
  (lambda (s1 s2)
    (cons s1 (cons s2 '()))))

(check-equal? (build 'bread 'butter) '(bread butter))

(define fun?
  (lambda (rel)
    (set? (firsts rel))))

(check-false (fun? '((4 3) (4 2) (7 6) (6 2) (3 4))))
(check-true (fun? '((8 3) (4 2) (7 6) (6 2) (3 4))))

(define revpair
  (lambda (pair)
    (build (second pair) (first pair))))

(define revrel
  (lambda (rel)
    (cond
      ((null? rel) '())
      (else (cons (revpair (car rel))
            (revrel (cdr rel)))))))

(check-equal? (revrel '((8 a) (pumpkin pie) (got sick)))
              '((a 8) (pie pumpkin) (sick got)))

(define seconds
  (lambda (l)
    (cond
      ((null? l) '())
      (else (cons (second (car l))
                  (seconds (cdr l)))))))

(check-equal? (seconds '((apple pie) (pineapple turt)))
              '(pie turt))

(define fullfun?
  (lambda (fun)
    (set? (seconds fun))))

(define one-to-one?
  (lambda (fun)
    (and (fun? fun) (fun? (revrel fun)))))

(check-true (one-to-one? '((a b) (b c) (c a))))

;; (begin
;;   (display "Hello Ash! It's working!!")
;;   (newline)(newline))




;;--------------------------------------------------------
;; Chapter 8 : Lambda the Ultimate
;;--------------------------------------------------------

(define eq?-c
  (lambda (a)
    (lambda (x)
      (eq? a x))))

(define eq?-salad (eq?-c 'salad))
(check-true (eq?-salad 'salad))
(check-false (eq?-salad 'tuna))


(define rember-f
  (lambda (test?)
      (lambda (a l)
        (cond
          ((null? l) '())
          ((test? a (car l)) (cdr l))
          (else (cons (car l) 
                      ((rember-f test?) a (cdr l))))))))

(define rember-eq? (rember-f eq?))
;; (rember-eq? '3 '(1 2 3 4 5))
(check-equal? (rember-eq? '3 '(1 2 3 4 5)) '(1 2 4 5))

(define rember-equal? (rember-f little-schemer-equal?))

(check-equal? (rember-equal? '(apple pie) '((banana cake) (pineapple turt) (apple pie) (mango bar)))
              '((banana cake) (pineapple turt) (mango bar)))

(define insertL-f
  (lambda (test?)
    (lambda (new old lat)
      (cond
        ((null? lat) '())
        ((test? (car lat) old) (cons new lat))
        (else (cons (car lat) 
                    ((insertL-f test?) new old (cdr lat))))))))

(define insertL-equal? (insertL-f little-schemer-equal?))

(check-equal? (insertL-equal? 'topping 'fudge '(ice cream with fudge for dessert))
              '(ice cream with topping fudge for dessert))


(check-equal? (insertL-equal? '(apple pie) '(mango bar) '((banana cake) (pineapple turt) (mango bar)))
              '((banana cake) (pineapple turt) (apple pie) (mango bar)))


;; Insert a new item after the first occurrence of an item (old) in the list
(define insertR-f
  (lambda (test?)
    (lambda (new old lat)
      (cond
        ((null? lat) '())
        ((test? (car lat) old) (cons old (cons new (cdr lat))))
        (else (cons (car lat) ((insertR-f test?) new old (cdr lat))))))))

(define insertR-equal? (insertR-f little-schemer-equal?))
(check-equal? (insertR-equal? '(apple pie) '(mango bar) '((banana cake) (pineapple turt) (mango bar)))
              '((banana cake) (pineapple turt) (mango bar) (apple pie)))


(define insert-g
  (lambda (seq)
    (lambda (new old l)
      (cond
        ((null? l) '())
        ((little-schemer-equal? old (car l)) (seq new old (cdr l)))
        (else (cons (car l) ((insert-g seq) new old (cdr l))))))))




;; Insert a new item after the first occurrence of an item (old) in the list
;; (define insertR
;;   (lambda (new old lat)
;;     (cond
;;       ((null? lat) '())
;;       ((eq? (car lat) old) (cons old (cons new (cdr lat))))
;;       (else (cons (car lat) (insertR new old (cdr lat)))))))
;; 

(define seqR
  (lambda (new old l)
    (cons old (cons new l))))

(check-equal? (seqR 'apple 'banana '(mango)) '(banana apple mango))

(define insertR (insert-g seqR))
(check-equal? (insertR '(apple pie) '(mango bar) '((banana cake) (pineapple turt) (mango bar)))
              '((banana cake) (pineapple turt) (mango bar) (apple pie)))
(check-equal? (insertR 'topping 'fudge '(ice cream with fudge for dessert))
              '(ice cream with fudge topping for dessert))


;; Insert a new item before the first occurrence of an item (old) in the list
;; (define insertL
;;   (lambda (new old lat)
;;     (cond
;;       ((null? lat) '())
;;       ((eq? (car lat) old) (cons new lat))
;;       (else (cons (car lat) (insertL new old (cdr lat)))))))
;; 

;;(insertL 'topping 'fudge '(ice cream with fudge for dessert))

(define seqL
  (lambda (new old l)
    (cons new (cons old l))))

(check-equal? (seqL 'apple 'banana '(mango)) '(apple banana mango))

;; (define insertL (insert-g seqL))

(define insertL
  (lambda (new old l)
    ((insert-g seqL) new old l)))

(check-equal? (insertL '(apple pie) '(mango bar) '((banana cake) (pineapple turt) (mango bar)))
              '((banana cake) (pineapple turt) (apple pie) (mango bar)))
(check-equal? (insertL 'topping 'fudge '(ice cream with fudge for dessert))
              '(ice cream with topping fudge for dessert))


;; Substitute the old item with new item on the first occurrence of an old item in the list


;; (define subst
;;   (lambda (new old lat)
;;     (cond
;;       ((null? lat) '())
;;       ((eq? (car lat) old) (cons new (cdr lat)))
;;       (else (cons (car lat) (subst new old (cdr lat)))))))
;; 

(define seqS
  (lambda (new old l)
    (cons new l)))

(define subst (insert-g seqS))

(check-equal? (subst 'topping 'fudge '(ice cream with fudge for dessert fudge))
              '(ice cream with topping for dessert fudge))


;; Redefining the rember function here
;; (define rember
;;   (lambda (s l)
;;     (cond
;;       ((null? l) '())
;;       ((little-schemer-equal? s (car l)) (cdr l))
;;       (else (cons (car l) (rember s (cdr l)))))))

(define seqRem
  (lambda (new old l)
    l))

(define rember
  (lambda (a l)
    ((insert-g seqRem) #f a l)))

(check-equal? '(Ashfaq Ur Rahman) (rember 'Quazi '(Quazi Ashfaq Ur Rahman)))
(check-equal? '(Quazi Ur Rahman) (rember 'Ashfaq '(Quazi Ashfaq Ur Rahman)))
(check-equal? '(Quazi Ashfaq Rahman) (rember 'Ur '(Quazi Ashfaq Ur Rahman)))
(check-equal? '(Quazi Ashfaq Ur) (rember 'Rahman '(Quazi Ashfaq Ur Rahman)))
(check-equal? '(Quazi Ashfaq Ur Rahman) (rember 'mango '(Quazi Ashfaq Ur Rahman)))


;;(check-equal? (multirember 5 '(5 mangoes 5 bananas 5 oranges)) '(mangoes bananas oranges)
(check-equal? '(Ur Rahman) (rember '(Quazi Ashfaq) '((Quazi Ashfaq) Ur Rahman)))


