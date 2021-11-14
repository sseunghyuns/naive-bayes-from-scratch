def get_row_num(csv_path):
    with open(csv_path) as file:
        return sum(1 for row in file)
    
def read_csv(csv_path, mode='train'):
    with open(csv_path) as file:
        result = {}
        total_rows = get_row_num(csv_path)
        label = csv_path.split("_")[-2]
        row_count = 0
        value = ''
        num=1
        # read line by line from .csv data. 
        for i in file:
            row_count+=1
            if row_count == total_rows:
                value = value + " " + i
                result.update({str(num) : value.replace("\n", "")})
            temp_val = i.split(",")
            if not len(temp_val)==1:
                if temp_val[1] == label: # 만약 row에서 ,로 split한 값이 spam이면, 해당 num 인덱스의 text값이 시작하는 row이다.
                    if mode == 'train':
                        if temp_val[0] == str(num+1):
                            result.update({str(num) : value.replace("\n", "")})

                            num+=1
                            value = i.split(f"{label},")[1] # spam, 이후부터가 text에 해당하는 값이므로, value 변수에 할당한다.
                            continue
                        else:
                            value = i.split(f"{label},")[1]
                            continue
                        
                    elif mode == 'test':
                        if int(i.split(f",{label}")[0].split(label[0])[1])== num+1:
                            result.update({str(num) : value.replace("\n", "")})
                            num+=1
                            value = i.split(f"{label},")[1] # spam, 이후부터가 text에 해당하는 값이므로, value 변수에 할당한다.
                            continue
                        else:
                            value = i.split(f"{label},")[1]
                            continue

            value = value + " " + i
            
    return {label: result}