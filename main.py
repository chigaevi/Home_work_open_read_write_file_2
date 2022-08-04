def counter_line(text):
    counter = 0
    for line in text:
        counter += 1
    return counter

with open('1.txt',encoding='utf-8') as one_text:
    quan_line_one = counter_line(one_text)
with open('2.txt', encoding='utf-8') as two_text:
    quan_line_two = counter_line(two_text)
with open('3.txt', encoding='utf-8') as three_text:
    quan_line_three = counter_line(three_text)


one_text = open('1.txt',encoding='utf-8')
two_text =  open('2.txt', encoding='utf-8')
three_text = open('3.txt', encoding='utf-8')

list_line = [quan_line_one, quan_line_two, quan_line_three]

with open('4.txt', 'w', encoding='utf-8') as final_text:
    for i_ in range(3):
        if quan_line_one == max(list_line):
            final_text.write(f'1.txt\n{quan_line_one}\n')
            for line in one_text:
                final_text.write(line)
            final_text.write('\n')
            list_line.remove(quan_line_one)

        elif quan_line_two == max(list_line):
            final_text.write(f'2.txt\n{quan_line_two}\n')
            for line in two_text:
                final_text.write(line)
            final_text.write('\n')
            list_line.remove(quan_line_two)

        elif quan_line_three == max(list_line):
            final_text.write(f'3.txt\n{quan_line_three}\n')
            for line in three_text:
                final_text.write(line)
            final_text.write('\n')
            list_line.remove(quan_line_three)

one_text.close()
two_text.close()
three_text.close()



