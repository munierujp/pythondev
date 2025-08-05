def fibonacci(n: int) -> int:
  """フィボナッチ数列を計算する関数"""

  if n <= 2:
    return 1
  else:
    return fibonacci(n - 2) + fibonacci(n - 1)