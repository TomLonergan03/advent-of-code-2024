import System.IO (readFile)
import Data.List (sort, subsequences)

filePath = "../input/day_2.txt"

parseLine :: String -> [Int]
parseLine line = map read (words line)

parseFile :: FilePath -> IO [[Int]]
parseFile filePath = do
    contents <- readFile filePath
    let linesOfFile = lines contents
    return $ map parseLine linesOfFile

countTrue :: [Bool] -> Int
countTrue xs = foldl (\acc x -> case x of { True -> acc + 1; False -> acc }) 0 xs

-- Part 1
countSafe :: [[Int]] -> Int
countSafe reports = countTrue $ map safe reports
    where safe xs = safePred (\(x,y) -> x < y && y - x <= 3) xs || safePred (\(x,y) -> x > y && x - y <= 3) xs
          safePred p xs = all p $ zip xs $ tail xs

-- Part 2
countSafeDampened :: [[Int]] -> Int
countSafeDampened reports = countTrue $ map safe reports
    where safe xs = safePred (\(x,y) -> x < y && y - x <= 3) xs || safePred (\(x,y) -> x > y && x - y <= 3) xs
          safePred :: ((Int, Int) -> Bool) -> [Int] -> Bool
          safePred p xs = (all p $ zip xs $ tail xs) || (any (all p) $ map (\x -> zip x $ tail x) [x | x <- subsequences xs, length x == length xs - 1])

main :: IO ()
main = do
    reports <- parseFile filePath
    putStr "Part 1: "
    print $ countSafe reports
    putStr "Part 2: "
    print $ countSafeDampened reports

