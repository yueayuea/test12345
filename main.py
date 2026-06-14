try:
    score = int(input('成績評價:'))
    if score < 0 or score >100:
         print('成績錯誤!重新輸入')
    elif score < 59:
          print('不及格')
    elif score < 75:
          print('及格')
    elif score < 85:
          print('良好')
    else:
          print('優秀')
except ValueError:
        print('成績錯誤!重新輸入')

print('感謝測試')
print('本句測試，查驗結果')
