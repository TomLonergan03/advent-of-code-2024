module Utils (parseFile) where

import System.IO (readFile)

parseFile :: FilePath -> (String -> a) -> IO [a]
parseFile filePath parseLine = do
  contents <- readFile $ filePath
  let linesOfFile = lines contents
  return $ map parseLine linesOfFile
