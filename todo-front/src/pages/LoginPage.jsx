import React, {useEffect, useState}from 'react'
import { useNavigate } from 'react-router-dom';

function LoginPage() {
    const API_URL = process.env.REACT_APP_API_URL
    const navigate = useNavigate();
    const [form, setform] = useState({
        username: '',
        password: '',
        error: null,
        isLoading: false,
    });

    // 🔁 Redirect if already logged in
    useEffect(() => {
        const token = localStorage.getItem('access');
        if (token) {
            navigate('/dashboard');
        }
    } ,[navigate]);

    // 🔄 Update form state
    const updateForm = (k,v) => {
        setform(prev => ({...prev, [k]: v}))

    }

    const handleSubmit = async (e) => {
        e.preventDefault();
        updateForm('error', null);
        updateForm('isLoading', true)

        try {
            const res = await fetch(`${API_URL}/api/token/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    username: form.username,
                    password: form.password,
                }),
            })
            
            if (!res.ok) {
                throw new Error('Login failed');
            }
            
            const data= await res.json();
            localStorage.setItem('access', data.token);
            localStorage.setItem('refresh', data.refresh);

            navigate('/dashboard');
        } catch (error) {
            updateForm('error', error.message);
        } finally {
            updateForm('isLoading', false);
        }
    }



  return (
     <div>
      <h2>Login</h2>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Username"
          value={form.username}
          onChange={(e) => updateForm('username', e.target.value)}
          required
        />

        <input
          type="password"
          placeholder="Password"
          value={form.password}
          onChange={(e) => updateForm('password', e.target.value)}
          required
        />

        <button type="submit" disabled={form.isLoading}>
          {form.isLoading ? 'Logging in...' : 'Login'}
        </button>
      </form>

      {form.error && <p style={{ color: 'red' }}>{form.error}</p>}
    </div>
  )
}

export default LoginPage