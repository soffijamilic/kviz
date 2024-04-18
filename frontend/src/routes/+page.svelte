<script lang="ts">
	import { goto } from '$app/navigation';
  
	function navigateTo(route: string) {
	  goto(route);
	}
  </script>
  
  <style>
	.navbar {
	  display: flex;
	  justify-content: space-between;
	  align-items: center;
	  padding: 1rem;
	  background-color: #333;
	  color: #fff;
	}
  
	.navbar button {
	  color: #fff;
	  text-decoration: none;
	  margin: 0 1rem;
	  padding: 0.5rem;
	  border: none;
	  background: none;
	  cursor: pointer;
	}
  
	.navbar button:hover {
	  background-color: #555;
	  border-radius: 5px;
	}
  </style>
  
  <div class="navbar">
	<button on:click="{() => navigateTo('Home')}">Home</button>
	<button on:click="{() => navigateTo('register')}">Register</button>
  </div>
<div class="container h-full mx-auto flex justify-center items-center">
	<div class="space-y-5">
		<h1 class="h1">Let's get cracking bones!</h1>
		<p>Start by exploring:</p>
		<ul>
			<li><code class="code">/src/routes/+layout.svelte</code> - barebones layout</li>
			<li><code class="code">/src/app.postcss</code> - app wide css</li>
			<li>
				<code class="code">/src/routes/+page.svelte</code> - this page, you can replace the contents
			
			
			</li>
		</ul>
	</div>
</div>

