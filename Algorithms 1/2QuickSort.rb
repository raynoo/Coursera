def sort(arr, first, last)
  if(first >= last)
    return
  end
  
  #by default it takes first element as pivot. so comment out line 9.
  #call pivotLast to take last element as pivot.
  #call pivotMedian to take the median as pivot.
  pivotMedian arr, first, last
  pivot = arr[first]
  index = first+1
  
  for j in (first+1)..last
    if arr[j] < pivot
      swap arr, index, j
      index += 1
    end
  end
  swap arr, index-1, first
  @count += (last-first)
  
  sort arr, first, index-2
  sort arr, index, last
end

def pivotLast arr, first, last
  swap arr, first, last
end

def pivotMedian arr, first, last
  a = { arr[first] => first, arr[(first+last)/2] => (first+last)/2, arr[last] => last}
  swap arr, first, a.sort.to_a()[1][1]
end

def swap arr, i1, i2
  temp = arr[i1]
  arr[i1] = arr[i2]
  arr[i2] = temp
end

def init
  arr = Array.new
  File.open('2input.txt', 'r').each_line do |line|
    arr.push(line.to_i);
  end
#  arr = [2, 8, 9, 3, 7, 5, 10, 1, 6, 4]
  return arr
end

@count = 0

arr = init
sort(arr, 0, arr.length()-1)

#puts arr
puts "\n"+@count.to_s