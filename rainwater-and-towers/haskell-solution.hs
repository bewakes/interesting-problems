-- looks sexy but is slower

rainfall :: [Int] -> Int
rainfall xs = sum (zipWith (-) mins xs)
  where
    mins = zipWith min maxl maxr
    maxl = scanl1 max xs
    maxr = scanr1 max xs
