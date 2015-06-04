module Vrypto

import Data.Fin
import Vrypto.Lang
import Vrypto.Syntax

-- End Syntax
cid : Crypto c (FunTy [4] [4])
cid = crypto $ (\x => x)

--instance Num (Crypto c (StreamTy n)) where
--    (+) = ?plus
--    (-) = ?sub
--    (*) = ?mult
--
--    abs = id
--    fromInteger i = Literal i

CInt : CType
CInt = [4]

Curry : List CType -> CType -> CType
Curry []      r = FunTy UnitTy r
Curry (x::xs) r = FunTy x (Curry xs r)

example : Crypto c CInt
example = crypto (pure cid <*> (Literal 1))

example2 : Crypto c [4]
example2 = crypto ([| (\x => x) (Literal 1) |])

head : Crypto c [S n] -> Crypto c [n]
head = ?head

--binaryMethod : Crypto c (Curry [[m], [e], [n]] [r])
--binaryMethod = crypto $ \m, e, n =>
--    let c = head e in ?rest


main : IO ()
main = putStrLn "Hello"
--computeBound : Bound -> Bound -> Bound
--computeBound Infinite b = b
--computeBound b Infinite = b
---- computeBound
--
--xor : BStream b1 a -> BStream b2 a -> BStream (computeBound b1 b2) a
--xor = ?xor
--
--fold : (Bool -> c -> c) -> c -> BStream n a -> c
--fold = ?fold
--
--chunk : (r : Nat) -> BStream n a -> List (BStream (Finite r) af)
--
--quaternary : BStream nM -> BStream ne -> BStream nn -> BStream r
--quaternary M e n = foldr $ map $ chunk 2 e
