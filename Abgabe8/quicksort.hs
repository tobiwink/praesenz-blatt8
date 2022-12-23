quicksort :: (Ord a) => [a] -> [a]
quicksort [] = []
quicksort (x:xs) =    quicksort (filter (<= x) xs)
                   ++ [x]
                   ++ quicksort (filter (> x) xs)


random_list :: Int -> [Double]
random_list n = [sin $ fromIntegral x | x <- [1..n]]