package math

type Counter struct {
	x int // приватное поле
}

func New() *Counter { return &Counter{} }

// Публично отдаём указатель на приватное поле
func (c *Counter) XPtr() *int { return &c.x }
