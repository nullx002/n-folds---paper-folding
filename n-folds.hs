    
    main = do

        putStrLn "thickness of the paper in mm:"
        t <- readLn
        let n1 =  t * 3.1415

        putStrLn "width of the paper in mm:"
        w <- readLn
        let n2 = w / n1

        let n3 = logBase 2 n2

        let n4 = 0.66667 * n3

        let n5 = 1 + n4

        let n6 = floor n5

        putStrLn ("number of possible folds are: " ++ show n6)
