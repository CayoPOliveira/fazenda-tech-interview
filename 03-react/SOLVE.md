<!-- @format -->

# FazendaTech - Programming Challenge

## 03 - React - Solving the problems from [README.md](README.md)

### Problem 01 - Dynamic React Component

1. What is the React rule that is being broken?

The "Rule of Hooks".

> Don’t call Hooks inside loops, conditions, nested functions, or try/catch/finally blocks.
> Instead, always use Hooks at the top level of your React function, before any early returns.
> You can only call Hooks while React is rendering a function component:
> ✅ Call them at the top level in the body of a function component.
> ✅ Call them at the top level in the body of a custom Hook.

Reference: [https://react.dev/reference/rules/rules-of-hooks](https://react.dev/reference/rules/rules-of-hooks).

2. How would you fix it?

To fix, I move the line `if` statement after the call of `useState`:

```tsx
import React, { useState } from "react";

interface Item {
	name: string;
	description: string;
}

interface ItemsCardProps {
	items: Item[];
}

export default function ItemsCard({ items }: ItemsCardProps) {
	//Call useState before if
	const [currentIndex, setCurrentIndex] = useState(0);

	// Handle empty items case
	if (items.length === 0) {
		return <div>No items!</div>;
	}

	const item = items[currentIndex];

	return (
		<div>
			<h3>
				Item #${currentIndex + 1} - {item.name}
			</h3>
			<span>{item.description}</span>
			<button onClick={() => setIndex((i) => (i + 1) % items.length)}>Next</button>
		</div>
	);
}
```

3. Why is this rule important?

React tracks the order calls of hooks between render, this ensures that React canmap ther state and effects correctly. If hooks are called that form, React may skip or change the order of hooks and cause problems, like inconsistent or incorrect state management and render behavior.

### Problem 02 - Rendering Arrays

1. What is the missing detail?

The `map` function forces the component to render all individual itens every time the array changes. This cause a re-render of some items that is not necessarily. React uses the `key` prop to optimize rendering by identifying which items in the list have changed. Since the current implementation is missing a key for each item in the list, React has no way of efficiently tracking which items are new, deleted, or moved, which forces a complete re-render of the list.

2. How would you implement it?

An easy way is just pass index of item as a key to the list.

```tsx
export default function ItemsList({ items }: ItemsListProps) {
	return (
		<div>
			{items.map((item, index) => (
				<div key={index}>
					<h3>{item.name}</h3>
					<span>{item.description}</span>
				</div>
			))}
		</div>
	);
}
```

This is a solution without changing the `Item` interface. If items are moved within the array, they will re-render and cause performance issues again, as deleting an item can change the index of all subsequent items.

3. Is there something you could add to the `Item` interface to make the solution better?

Can be add an unique identifier to `Item` that can be used to map themselves.

```tsx
import React from "react";

interface Item {
	id: number;
	name: string;
	description: string;
}

interface ItemsListProps {
	items: Item[];
}

export default function ItemsList({ items }: ItemsListProps) {
	return (
		<div>
			{items.map((item) => (
				<div key={item.id}>
					<h3>{item.name}</h3>
					<span>{item.description}</span>
				</div>
			))}
		</div>
	);
}
```
