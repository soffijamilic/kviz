<script lang="ts">
    import { onMount } from 'svelte';
    import { goto } from '$app/navigation';
  
    let email = '';
    let username = '';
    let password = '';
  
    async function handleSubmit(event: Event) {
      event.preventDefault();
      const data = {
      email: email,
      username: username,
      password: password
    };

    console.log('Request data:', data);

    const response = await fetch('http://localhost:5000/auth/register', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin' : 'http://localhost:5000'
      },
      body: JSON.stringify(data)
    });

    console.log('Response status:', response.status);
    console.log('Response status text:', response.statusText);
      // Perform registration logic here
      // For example, send a request to your server with the registration data
  
      // After successful registration, navigate to the desired page
      goto('/login');
       
    }
    
  </script>
  <div class="container h-full mx-auto flex justify-center items-center">
  <form on:submit="{handleSubmit}">
    <label for="email">Email</label>
    <input id="email" type="email" bind:value="{email}" required />
  
    <label for="username">Username</label>
    <input id="username" type="text" bind:value="{username}" required />
  
    <label for="password">Password</label>
    <input id="password" type="password" bind:value="{password}" required />
  
    <button type="submit">Register</button>
  </form>
</div>