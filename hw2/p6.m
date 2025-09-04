function x = cal_band(A, b, w)
    n = length(b);

    % forward elimination
    for i = 1:n-1
        for j = i+1:min(i+w, n)
            if abs(A(i,i)) < 1e-12
                error("Zero pivot at row %d", i);
            end
            mul = A(j, i) / A(i, i);
            for k = i:min(i+w, n)
                A(j, k) = A(j, k) - mul * A(i,k);
            end
            b(j) = b(j) - mul * b(i); 
        end
    end

    % back substitution
    x = zeros(n,1);
    for i = n:-1:1
        s = 0;
        for j = i+1:min(i+w, n)
            s = s + A(i,j)*x(j);
        end
        x(i) = (b(i) - s) / A(i,i);
    end
end
