import System.IO (readFile)
import Data.List (sort)

-- Function to parse a line into an (Int, Int) pair
parseLine :: String -> (Int, Int)
parseLine line = 
    let [x, y] = map read (words line)
    in (x, y)

-- Function to read the file and parse it into a list of (Int, Int) pairs
readFileIntoPairs :: FilePath -> IO [(Int, Int)]
readFileIntoPairs filePath = do
    contents <- readFile filePath
    let linesOfFile = lines contents
    return $ map parseLine linesOfFile

-- Part 1
distance :: ([Int], [Int]) -> Int
distance (a, b) = sum $ map (\x -> abs (fst x - snd x)) $ zip (sort a) (sort b)

-- Part 2
similarity :: ([Int], [Int]) -> Int
similarity (a, b) = sum $ map (\x -> x * count x b) a
    where count x xs = length $ filter (== x) xs

-- Example usage
main :: IO ()
main = do
    pairs <- readFileIntoPairs "../input/day_1.txt"
    putStr "Part 1: "
    print $ distance $ unzip pairs
    putStr "Part 2: "
    print $ similarity $ unzip pairs
