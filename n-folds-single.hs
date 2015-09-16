
    main = do

        putStrLn "thickness of the paper in mm:"
        t <- getLine >>= readIO . ('0' : ) 
        let n1 = (2 *  t * sqrt 3.1415)

        putStrLn "length of the paper in mm:"
        l <- readLn

        let n2 = logBase 2.71828 ( ( ( sqrt ( (24 * t * l) + (25 * 3.1415 * t^2) ) ) / n1 ) - 0.66667)

        let n3 = logBase 2.71828 2

        let n4 = n2 / n3

        let n5 = floor n4

        putStrLn ("number of possible folds are: " ++ show n5)
