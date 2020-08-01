  #include <cstdio>
  #include <random>
  #include "/home/nanoproj/michael/gem5/include/gem5/m5ops.h"
  #include "/home/nanoproj/michael/gem5/util/m5/src/m5_mmap.h"

  int main()
  {
    m5_dump_reset_stats(0, 0);
    const int N = 1000;
    double X[N], Y[N], alpha = 0.5;
    std::random_device rd; std::mt19937 gen(rd());
    std::uniform_real_distribution<> dis(1, 2);

    for (int i = 0; i < N; ++i)
    {
      X[i] = dis(gen);
      Y[i] = dis(gen);
    }

    // Start of daxpy loop
    m5_dump_reset_stats(0, 0);
    for (int i = 0; i < N; ++i)
    {
      Y[i] = alpha * X[i] + Y[i];
    }
    m5_dump_reset_stats(0, 0);
    // End of daxpy loop

    double sum = 0;
    for (int i = 0; i < N; ++i)
    {
      sum += Y[i];
    }
    printf("%lf\n", sum);
    return 0; 
  }