module Utils (parseFile, countTrue) where

import System.IO (readFile)

parseFile :: FilePath -> (String -> a) -> IO [a]
parseFile filePath parseLine = do
  contents <- readFile $ filePath
  let linesOfFile = lines contents
  return $ map parseLine linesOfFile

countTrue :: [Bool] -> Int
countTrue xs = foldl (\acc x -> case x of True -> acc + 1; False -> acc) 0 xs
