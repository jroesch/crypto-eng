module Vrypto.Lang

import Data.Fin
import Data.Vect
import Data.HVect

mutual
    data CType : Type where
        UnitTy   : CType
        BitTy    : CType
        StreamTy : Nat -> CType -> CType
        TupleTy  : Vect n a -> CType
        -- RecordTy : HVect
        FunTy    : CType -> CType -> CType

    Context : Nat -> Type
    Context n = Vect n CType

    data HasType : (i : Fin n) -> Vect n CType -> CType -> Type where
        Stop : HasType FZ (t :: ctxt) t
        Pop  : HasType k ctxt t -> HasType (FS k) (u :: ctxt) t

    data Width : Type -> Nat -> Type where
        IntWidth : Width Int 4

    data Sized : Nat -> (Type -> Type) -> Type -> Type where
        
    data Crypto : Context n -> CType -> Type where
        Literal : {auto w : Width t n} -> t -> Crypto c (StreamTy n BitTy)
        Var     : HasType i c t -> Crypto c t
        Lam     : Crypto (x :: c) t -> Crypto c (FunTy x t)
        App     : Crypto c (FunTy a t) -> Crypto c a -> Crypto c t
        Project : {auto p : Sized n t a} -> (i : Fin n) -> t -> Crypto c a
