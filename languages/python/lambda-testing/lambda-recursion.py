#!/usr/bin/env python3

# (define print_result
#   (lambda (lat L R)
#     (writeln (quasiquote ("End Result:" (,lat ,L ,R))))))
# 
# 
# (define multiinsertLR&Co
#   (lambda (newitem oldL oldR lat col)
#     (cond
#       ((null? lat)
#        (writeln "At last found emepty list!!" )
#        (col '() 0 0))
#       ((eq? (car lat) oldL)
#                           (fprintf (current-output-port) "oldL = ~a\n" oldL)
#                           (multiinsertLR&Co newitem oldL oldR (cdr lat)
#                                                                     (lambda (newlat L R)
#                                                                       (fprintf (current-output-port) "Item:~a, lat:~a, newlat:~a, L:~a, R:~a\n"
#                                                                                 oldL lat newlat L R)
#                                                                       (col (cons newitem (cons oldL newlat)) (add1 L) R)))))
#                           (fprintf (current-output-port) "Came back here: oldL = ~a\n" oldL)
#       )
#       ((eq? (car lat) oldR)
#                           (fprintf (current-output-port) "oldR = ~a\n" oldR)
#                           (multiinsertLR&Co newitem oldL oldR (cdr lat)
#                                                                     (lambda (newlat L R)
#                                                                       (fprintf (current-output-port) "Item:~a, lat:~a, newlat:~a, L:~a, R:~a\n"
#                                                                                 oldR lat newlat L R)
#                                                                       (col (cons oldR (cons newitem newlat)) L (add1 R))))))
#                           (fprintf (current-output-port) "Came back here: oldR = ~a\n" oldR)
#       )
#       (else
#           (fprintf (current-output-port) "Didn't match :~a\n" (car lat))
#           (cons (car lat) (multiinsertLR&Co newitem oldL oldR (cdr lat)
#                                            (lambda (newlat L R)
#                                              (fprintf (current-output-port) "Item:~a, lat:~a, newlat:~a, L:~a, R:~a\n"
#                                                       (car lat) lat newlat L R)
#                                              (col (cons (car lat) newlat) L R))))
#           (fprintf (current-output-port) "Came back here: Didn't match :~a\n" (car lat))
#       ))))
# 
# (multiinsertLR&Co 'apple 'banana 'mango '(strawberry banana mango banana) print_result)
# 
# 


def print_result (lat, L, R):
    print (f"End Result: lat:{lat} L:{L} R:{R}")

def multiinsertLRCo (newItem, oldL, oldR, lat, collector_function):
    if lat == []:
        collector_function([], 0, 0)
    elif lat[0] == oldL:
        multiinsertLRCo(newItem, oldL, oldR, lat[0:], lambda newlat,oldL,oldR: collector_function([newitem, oldL]+newlat, L+1, R))
    elif lat[0] == oldR:
        multiinsertLRCo(newItem, oldL, oldR, lat[0:], lambda newlat,oldL,oldR: collector_function([oldR,newitem]+newlat, L, R+1))
    else:
        multiinsertLRCo(newItem, oldL, oldR, lat[0:], lambda newlat,oldL,oldR: collector_function([lat[0]]+newlat, L, R))



multiinsertLRCo('apple', 'banana', 'mango', ['strawberry', 'banana', 'mango', 'banana'], print_result)

# print_result(['strawberry', 'banana', 'mango', 'banana'], 100, 1000)

