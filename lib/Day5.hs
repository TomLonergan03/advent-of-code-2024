module Day5 (run) where

import Data.HashMap.Strict (HashMap, fromList, member, (!))
import Data.List.Split (splitOn)
import Utils (parseFile)

filePath = "input/day_5.txt"

isInOrder :: [(Int, Int)] -> [Int] -> Bool
isInOrder page_rules page_order = all (\page -> all id [elem p $ takeWhile (/= page) page_order | p <- map fst $ pagesThatMustComeBefore page_rules page_order page]) page_order

pagesThatMustComeBefore :: [(Int, Int)] -> [Int] -> Int -> [(Int, Int)]
pagesThatMustComeBefore page_rules pages page = filter (\(a, b) -> b == page && a `elem` pages) page_rules

score :: [[Int]] -> Int
score page_order = sum $ map (\pages -> pages !! (length pages `div` 2)) page_order

-- Part 1
findOrdered :: [(Int, Int)] -> [[Int]] -> Int
findOrdered page_rules page_order = score $ filter (isInOrder page_rules) page_order

-- Part 2
fixUnordered :: [(Int, Int)] -> [[Int]] -> Int
fixUnordered page_rules page_order = score $ map (fixUnordered' page_rules) $ filter (not . isInOrder page_rules) page_order
  where
    fixUnordered' :: [(Int, Int)] -> [Int] -> [Int]
    fixUnordered' page_rules page_order = if isInOrder page_rules page_order then page_order else fixUnordered' page_rules $ makeSwap page_rules page_order
    makeSwap :: [(Int, Int)] -> [Int] -> [Int]
    makeSwap page_rules page_order =
      -- TODO: find the first page that is out of order and fix that
      let (a, b) = outOfOrderPage page_rules page_order
       in swap a b page_order
    swap :: Int -> Int -> [Int] -> [Int]
    swap a b xs = map (\x -> if x == a then b else if x == b then a else x) xs

run :: IO ()
run = do
  instructionString <- parseFile filePath id
  let page_rules = map (\s -> (read $ take 2 s, read $ drop 3 s)) $ takeWhile (/= "") instructionString :: [(Int, Int)]
  let page_order = map (map read . splitOn ",") $ drop 1 $ dropWhile (/= "") instructionString :: [[Int]]
  putStr "Part 1: "
  print $ findOrdered page_rules page_order
  putStr "Part 2: "
  print $ fixUnordered page_rules page_order
