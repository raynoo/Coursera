class Stack
  def initialize
   @stack = []
  end

  def peek
    @stack[-1]
  end
  
  def push(item)
    @stack.push item
  end

  def pop
    @stack.pop
  end

  def size
    @stack.length
  end
  
  def empty?
    @stack.length() == 0
  end
end