#lang racket


(define print_result
  (lambda (lat L R)
    (writeln (quasiquote ("End Result:" (,lat ,L ,R))))))


(define multiinsertLR&Co
  (lambda (newitem oldL oldR lat col)
    (cond
      ((null? lat)
       (writeln "At last found emepty list!!" )
       (col '() 0 0))
      ((eq? (car lat) oldL) 
                          (fprintf (current-output-port) "oldL = ~a\n" oldL)
                          (multiinsertLR&Co newitem oldL oldR (cdr lat)
                                            (lambda (newlat L R)
                                              (fprintf (current-output-port) "Item:~a, lat:~a, newlat:~a, L:~a, R:~a\n" oldL lat newlat L R)
                                              (col (cons newitem (cons oldL newlat)) (add1 L) R)))
                          (fprintf (current-output-port) "Came back here: oldL = ~a\n" oldL)
      )
      ((eq? (car lat) oldR) 
                          (fprintf (current-output-port) "oldR = ~a\n" oldR)
                          (multiinsertLR&Co newitem oldL oldR (cdr lat)
                                            (lambda (newlat L R)
                                              (fprintf (current-output-port) "Item:~a, lat:~a, newlat:~a, L:~a, R:~a\n" oldR lat newlat L R)
                                              (col (cons oldR (cons newitem newlat)) L (add1 R))))
                          (fprintf (current-output-port) "Came back here: oldR = ~a\n" oldR)
      )
      (else 
          (fprintf (current-output-port) "Didn't match :~a\n" (car lat))
          (cons (car lat) (multiinsertLR&Co newitem oldL oldR (cdr lat)
                                           (lambda (newlat L R)
                                             (fprintf (current-output-port) "Item:~a, lat:~a, newlat:~a, L:~a, R:~a\n"
                                                      (car lat) lat newlat L R)
                                             (col (cons (car lat) newlat) L R))))
          (fprintf (current-output-port) "Came back here: Didn't match :~a\n" (car lat))
      ))))

(multiinsertLR&Co 'apple 'banana 'mango '(strawberry banana mango banana) print_result)


