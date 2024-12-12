module Day3 (run) where

import Text.Regex.PCRE
import Utils (parseFile)

filePath = "input/day_3.txt"

-- Part 1
findMul :: String -> Int
findMul s =
  foldl (\acc [a, b] -> acc + a * b) 0 $
    map ((\x -> map (read :: String -> Int) $ getAllTextMatches (x =~ "[0-9]+")) :: String -> [Int]) $
      getAllTextMatches (s =~ "mul\\([0-9]+,[0-9]+\\)") -- match everything that looks like mul(a, b)

-- Part 2
findMulWithStops :: String -> Int
findMulWithStops s =
  findMul $ -- we can reuse the findMul function once all invalid instructions are removed
    (concat :: [String] -> String) $
      -- match everything between the start of the line and the first don't(),
      -- between any do() and don't() and between the last don't() and the end of the line
      getAllTextMatches (s =~ "(^.*?|(?<=do\\(\\))).*?(?=don't\\(\\).*?|(?=$))")

run :: IO ()
run = do
  instructionString <- parseFile filePath id
  putStr "Part 1: "
  print $ findMul $ concat instructionString
  putStr "Part 2: "
  print $ findMulWithStops $ concat instructionString
