
-- QuickSort
--  - Parameter: Liste der zu sortierenden Elemente
--
--  - Liefert: Sortierte Liste

quicksort :: (Ord a) => [a] -> [a]
quicksort [] = []
quicksort (x:xs) =    quicksort (filter (<= x) xs)
                   ++ [x]
                   ++ quicksort (filter (> x) xs)


-- Random List
--  - Parameter: Anzahl der Elemente
--
--  - Liefert: Liste mit (zufaelligen) Elementen
--            (hier: Sinusfunktion, welche genuegend zufaellige Werte liefert)
random_list :: Int -> [Double]
random_list n = [sin $ fromIntegral x | x <- [1..n]]