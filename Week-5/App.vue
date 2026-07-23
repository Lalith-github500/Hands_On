<!--
  App.vue
  Week 5 - Frontend Frameworks
  Demonstrates: Vue 3 reactivity system using `ref` and `computed`
  via the Composition API - a searchable / filterable product list.

  To run:
    npm create vue@latest my-vue-app
    cd my-vue-app
    npm install
    Replace src/App.vue with this file, then `npm run dev`
-->

<template>
  <div class="app">
    <h1>Product Catalog</h1>

    <!-- v-model creates two-way binding to the reactive `searchTerm` ref -->
    <input
      v-model="searchTerm"
      type="text"
      placeholder="Search products..."
      class="search-box"
    />

    <!-- v-model bound to category filter -->
    <select v-model="selectedCategory">
      <option value="All">All Categories</option>
      <option v-for="cat in categories" :key="cat" :value="cat">
        {{ cat }}
      </option>
    </select>

    <p class="result-count">{{ filteredProducts.length }} result(s) found</p>

    <ul class="product-list">
      <li v-for="product in filteredProducts" :key="product.id">
        <span class="name">{{ product.name }}</span>
        <span class="category">{{ product.category }}</span>
        <span class="price">${{ product.price.toFixed(2) }}</span>
      </li>
    </ul>

    <p v-if="filteredProducts.length === 0" class="empty">
      No products match your search.
    </p>
  </div>
</template>

<script setup>
import { ref, computed } from "vue";

// --- Reactive state (ref) ---------------------------------
// `ref` wraps a value so Vue can track reads/writes to it and
// automatically re-render any part of the template that uses it.
const searchTerm = ref("");
const selectedCategory = ref("All");

const products = ref([
  { id: 1, name: "Wireless Mouse", category: "Electronics", price: 19.99 },
  { id: 2, name: "Mechanical Keyboard", category: "Electronics", price: 59.99 },
  { id: 3, name: "Yoga Mat", category: "Fitness", price: 24.5 },
  { id: 4, name: "Water Bottle", category: "Fitness", price: 12.0 },
  { id: 5, name: "Notebook", category: "Office", price: 3.5 },
  { id: 6, name: "Desk Lamp", category: "Office", price: 15.75 },
]);

// --- Derived state (computed) ------------------------------
// `computed` creates a cached, reactive value that automatically
// recalculates only when one of its dependencies (searchTerm,
// selectedCategory, products) changes.
const categories = computed(() => {
  const unique = new Set(products.value.map((p) => p.category));
  return [...unique];
});

const filteredProducts = computed(() => {
  return products.value.filter((product) => {
    const matchesSearch = product.name
      .toLowerCase()
      .includes(searchTerm.value.toLowerCase());
    const matchesCategory =
      selectedCategory.value === "All" ||
      product.category === selectedCategory.value;
    return matchesSearch && matchesCategory;
  });
});
</script>

<style scoped>
.app {
  max-width: 500px;
  margin: 2rem auto;
  font-family: sans-serif;
}
.search-box,
select {
  width: 100%;
  padding: 0.5rem;
  margin-bottom: 0.75rem;
  box-sizing: border-box;
}
.product-list {
  list-style: none;
  padding: 0;
}
.product-list li {
  display: flex;
  justify-content: space-between;
  padding: 0.5rem;
  border-bottom: 1px solid #eee;
}
.result-count {
  color: #666;
  font-size: 0.9rem;
}
.empty {
  color: #999;
  font-style: italic;
}
</style>
