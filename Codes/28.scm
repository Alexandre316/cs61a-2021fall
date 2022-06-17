; Quasiquotation

; Sum the squares of even numbers less than 10, starting with 2
; x = 2
; total = 0
; while x < 10:
;     total = total + x * x
;     x = x + 2
; RESULT: 2 * 2 + 4 * 4 + 6 * 6 + 8 * 8 = 120

(begin
  (define (f x total)
    (if (< x 10)
      (f (+ x 2) (+ total (* x x)))
      total))
  (f 2 0))
  
; Sum the numbers whose squares are less than 50, starting with 1
; x = 1
; total = 0
; while x * x < 50:
; 	total = total + x
;       x = x + 1
; RESULT: 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28

(begin
  (define (f x total)
    (if (< (* x x) 50)
      (f (+ x 1) (+ total x))
      total))
  (f 1 0))

(define   (sum-while starting-x while-condition add-to-total update-x)
  ; (eval (sum-while 2          '(< x 10)       '(* x x)     '(+ x 2)))  =>  120
  ; (eval (sum-while 1          '(< (* x x) 50) 'x           '(+ x 1)))  =>  28
  `(begin
     (define (f x total)
       (if ,while-condition
         (f ,update-x (+ total ,add-to-total))
         total))
     (f ,starting-x 0)))
