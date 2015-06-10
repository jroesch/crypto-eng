module Vrypto.Syntax

import Vrypto.Lang

mkLambda : TTName -> Crypto (a :: c) t -> Crypto c (FunTy a t)
mkLambda _ body = Lam body

-- Syntax
(<*>) : (f : Lazy (Crypto c (FunTy a t))) -> Crypto c a -> Crypto c t
(<*>) f a = App f a

pure : {t : CType} -> Crypto c t -> Crypto c t
pure = id

dsl crypto
    variable    = Var
    index_first = Stop
    index_next  = Pop
    lambda      = mkLambda

syntax "[" [nat] "]" = StreamTy nat BitTy

syntax "|" [arg] "==>" [result] "|" = FunTy arg result

-- project : Crypto 
