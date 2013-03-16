##test case: 1test.txt
##solution: 2507223936

##assignment: 1input.txt
##solution: 2407905288

#initialize nxn array with random values
def init input
  File.open('1input.txt', 'r').each_line do |line|
    input.push(line.to_i);
  end
end

#recursive call until 1 element in array
def count input, first, last
#  puts first.to_s() + " " + last.to_s()
  
  return if first == last
  
  mid = (first+last)/2
  
  count(input, first, mid)
  count(input, mid+1, last)
  mergeAndCountSplit(input, first, last)
  
end

#merge sort and count the inversions (left, right and splits)
#(in this case all the inversions will be splits as we are counting
# at merge of already sorted arrays, right?)
def mergeAndCountSplit input, first, last
  
  i1 = first
  mid = ((first+last)/2)
  i2 = mid+1
  tempArray = []
  i = 0
  
  if last-first == 1
    if input[first].to_i > input[last].to_i
      @inv += 1
      swap input, first, last
    end
    return
  end
  
  until i1 == mid+1 or i2 == last+1
    if input[i1].to_i <= input[i2].to_i
      tempArray[i] = input[i1]
      i += 1
      i1 += 1
    else
      @inv += mid+1-i1
      tempArray[i] = input[i2]
      i += 1
      i2 += 1
    end
  end
  

  if !tempArray.empty?
    if i1 < mid+1
      until i1 == mid+1
        tempArray[i] = input[i1]; i1+=1; i+=1
      end
    end
    if i2 < last+1
      until i2 == last+1
        tempArray[i] = input[i2]; i2+=1; i+=1
        end
    end
  
    i = 0
    for j in first..last
      input[j] = tempArray[i]
      i += 1
    end
  end

end

def swap input, i, j
  temp = input[i]
  input[i] = input[j]
  input[j] = temp
end

@inv = 0
input = [1, 10, 2, 15, 20]
init input
#puts "Initial "
#puts input
#puts "\n"

count input, 0, input.size()-1

puts @inv

#puts "\nFinal "
#puts input