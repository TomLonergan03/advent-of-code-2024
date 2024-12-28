module Day2 (run) where

import Data.List (subsequences)
import Utils (countTrue, parseFile)

filePath = "../input/day_2.txt"

parseLine :: String -> [Int]
parseLine line = map read (words line)

-- Part 1
countSafe :: [[Int]] -> Int
countSafe reports = countTrue $ map safe reports
  where
    safe xs = safePred (\(x, y) -> x < y && y - x <= 3) xs || safePred (\(x, y) -> x > y && x - y <= 3) xs
    safePred p xs = all p $ zip xs $ tail xs

-- Part 2
countSafeDampened :: [[Int]] -> Int
countSafeDampened reports = countTrue $ map safe reports
  where
    safe xs = safePred (\(x, y) -> x < y && y - x <= 3) xs || safePred (\(x, y) -> x > y && x - y <= 3) xs
    safePred :: ((Int, Int) -> Bool) -> [Int] -> Bool
    safePred p xs = (all p $ zip xs $ tail xs) || (any (all p) $ map (\x -> zip x $ tail x) [x | x <- subsequences xs, length x == length xs - 1])

run :: IO ()
run = do
  reports <- parseFile filePath parseLine
  putStr "Part 1: "
  print $ countSafe reports
  putStr "Part 2: "
  print $ countSafeDampened reports
