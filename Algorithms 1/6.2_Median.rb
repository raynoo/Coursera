#Implementation of Running Median (or Median Maintenance) algorithm
# to determine median of a set of running numbers.
#Implemented using 2 heaps, a MaxHeap for lower half of input
# and a MinHeap for higher half input.

require 'algorithms'
require 'set'
include Containers

def init
  @arr = Array.new
  File.open('6input2.txt', 'r').each_line do |line|
    @arr.push(line.to_i);
  end
  
  @lowerhalf = MaxHeap.new()
  @higherhalf = MinHeap.new()
  
  @running_median = 0
end

#insert input into heap one at a time and get the median
def start
  @arr.each { |input|
    insert input
    
    @running_median += get_median
#    puts "#{@lowerhalf.size}, #{@higherhalf.size}"
#    puts "Input #{input} Lower #{@lowerhalf.max} Higher #{@higherhalf.min} Median #{get_median}"
  }
  p @running_median % 10000
end

#insert into appropriate heap
def insert input
  if @lowerhalf.empty? or input < @lowerhalf.max
    @lowerhalf.push input
  else
    @higherhalf.push input
  end
  
  check_balance  
end

#the 2 heaps have to be of equal size.
#so adjust the size of the 2 heaps if one is
#bigger than the other by more than 1 element.
def check_balance
  until (@lowerhalf.size - @higherhalf.size).abs <= 1
    if @lowerhalf.size > @higherhalf.size
      @higherhalf.push @lowerhalf.pop
    else
      @lowerhalf.push @higherhalf.pop
    end
  end
end

#the median is the top element of the larger heap.
def get_median
  if @lowerhalf.size >= @higherhalf.size
    return @lowerhalf.max
  else
    return @higherhalf.min
  end
end

init
start