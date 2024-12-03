module Day1 (run) where

import Data.List (sort)
import Utils (parseFile)

parseLine :: String -> (Int, Int)
parseLine line = 
    let [x, y] = map read (words line)
    in (x, y)

-- Part 1
distance :: ([Int], [Int]) -> Int
distance (a, b) = sum $ map (\x -> abs (fst x - snd x)) $ zip (sort a) (sort b)

-- Part 2
similarity :: ([Int], [Int]) -> Int
similarity (a, b) = sum $ map (\x -> x * count x b) a
    where count x xs = length $ filter (== x) xs

run :: IO ()
run = do
    pairs <- parseFile "input/day_1.txt" parseLine
    putStr "Part 1: "
    print $ distance $ unzip pairs
    putStr "Part 2: "
    print $ similarity $ unzip pairs

