module Main where

import qualified Day1
import qualified Day2
import qualified Day3
import qualified Day4

main :: IO ()
main = do
  putStrLn "\nDay 1"
  Day1.run
  putStrLn "Day 2"
  Day2.run
  putStrLn "Day 3"
  Day3.run
  putStrLn "Day 4"
  Day4.run
  putStrLn ""
