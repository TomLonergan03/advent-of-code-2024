module Day4 (run) where

import Data.List (isPrefixOf, transpose)
import Utils (countTrue, parseFile)

filePath = "input/day_4.txt"

getAllDiagonals :: [String] -> [String]
getAllDiagonals m = getAllDiagonals' m ++ getAllDiagonals' (map reverse m)
  where
    getAllDiagonals' m = [[m !! y !! x | (x, y) <- zip [start_x .. length m - 1] [start_y .. length m - 1]] | (start_x, start_y) <- getStarts m]
    getStarts m = [(start_x, start_y) | (start_x, start_y) <- zip [max 0 x | x <- reverse [-length m + 1 .. length m - 1]] [max 0 x | x <- [-length m + 1 .. length m - 1]]]

-- Part 1
findAllXmas :: [String] -> Int
findAllXmas ss = sum $ map countXmas $ inputStrings ss
  where
    inputStrings :: [String] -> [String]
    inputStrings ss = ss ++ transpose ss ++ getAllDiagonals ss

    countXmas :: String -> Int
    countXmas x = if x == [] then 0 else if "XMAS" `isPrefixOf` x || "SAMX" `isPrefixOf` x then 1 + (countXmas $ tail x) else countXmas $ tail x

-- Part 2
findAllX_mas :: [String] -> Int
findAllX_mas ss = countTrue $ map (isX_mas . getAllDiagonals . square ss) $ squareCorners ss
  where
    squareCorners :: [String] -> [(Int, Int)]
    squareCorners ss = [(x - 1, y - 1) | x <- [0 .. length ss - 1], y <- [0 .. length ss - 1], ss !! x !! y == 'A', x > 0, x < length ss - 1, y > 0, y < length ss - 1]

    square :: [String] -> (Int, Int) -> [String]
    square ss (x, y) = map (\s -> take 3 $ drop (y) s) $ take 3 $ drop x ss

    isX_mas :: [String] -> Bool
    isX_mas diagonals = all (\x -> x == "MAS" || x == "SAM") $ filter (\x -> length x == 3) diagonals

run :: IO ()
run = do
  instructionString <- parseFile filePath id
  putStr "Part 1: "
  print $ findAllXmas instructionString
  putStr "Part 2: "
  print $ findAllX_mas instructionString
