<script lang="ts">
  let email = '';
  let password = '';

  async function handleSubmit(event: Event) {
    event.preventDefault();

    // Perform login logic here
    // For example, send a request to your server with the login data

    // After successful login, navigate to the desired page
    // goto('/dashboard');
  }
</script>

<style>
  .login-form {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-top: 5rem;
  }

  .login-form label {
    margin-bottom: 0.5rem;
  }

  .login-form input {
    margin-bottom: 1rem;
    padding: 0.5rem;
  }

  .login-form button {
    padding: 0.5rem;
    cursor: pointer;
  }
</style>

<div class="login-form">
  <h1>Login</h1>
  <form on:submit="{handleSubmit}">
    <label for="email">Email</label>
    <input id="email" type="email" bind:value="{email}" required />

    <label for="password">Password</label>
    <input id="password" type="password" bind:value="{password}" required />

    <button type="submit">Login</button>
  </form>
</div>
