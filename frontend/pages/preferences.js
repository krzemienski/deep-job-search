import { useState, useEffect } from 'react';
import { useRouter } from 'next/router';
import Head from 'next/head';
import {
  Container,
  Typography,
  Button,
  Box,
  Paper,
  TextField,
  MenuItem,
  Alert,
  CircularProgress,
} from '@mui/material';
import { WorkOutline } from '@mui/icons-material';
import { createTheme, ThemeProvider } from '@mui/material/styles';

const companySizes = [
  { value: 'Any', label: 'Any Size' },
  { value: 'Startup', label: 'Startup (1-50)' },
  { value: 'Small', label: 'Small (51-200)' },
  { value: 'Medium', label: 'Medium (201-1000)' },
  { value: 'Large', label: 'Large (1000+)' },
];

const darkTheme = createTheme({
  palette: {
    mode: 'dark',
  },
});

export default function Preferences() {
  const router = useRouter();
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);
  const [preferences, setPreferences] = useState({
    location: '',
    company_size: 'Any',
    role_type: '',
    additional_info: '',
  });

  useEffect(() => {
    const summary = sessionStorage.getItem('resumeSummary');
    if (!summary) {
      router.replace('/resume-upload');
    }
  }, [router]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setIsLoading(true);
    setError(null);

    try {
      const response = await fetch(
        `${process.env.NEXT_PUBLIC_API_URL}/api/deep_search`,
        {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            resume_summary: JSON.parse(sessionStorage.getItem('resumeSummary')),
            preferences: preferences,
          }),
        }
      );

      if (!response.ok) {
        throw new Error('Failed to start job search');
      }

      const data = await response.json();
      sessionStorage.setItem('taskId', data.task_id);
      router.push('/results');
    } catch (err) {
      setError(err.message);
    } finally {
      setIsLoading(false);
    }
  };

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setPreferences((prev) => ({
      ...prev,
      [name]: value,
    }));
  };

  return (
    <ThemeProvider theme={darkTheme}>
      <Head>
        <title>Job Preferences - Deep Job Search</title>
      </Head>

      <Container maxWidth="md">
        <Box sx={{ my: 4 }}>
          <Typography
            variant="h3"
            component="h1"
            gutterBottom
            align="center"
            sx={{ mb: 4 }}
          >
            Set Your Job Preferences
          </Typography>

          <Paper sx={{ p: 4 }}>
            {error && (
              <Alert severity="error" sx={{ mb: 3 }}>
                {error}
              </Alert>
            )}

            <Box component="form" onSubmit={handleSubmit}>
              <TextField
                fullWidth
                label="Preferred Location"
                name="location"
                value={preferences.location}
                onChange={handleInputChange}
                required
                sx={{ mb: 3 }}
                placeholder="e.g., Remote, New York, London"
                InputProps={{
                  startAdornment: (
                    <WorkOutline sx={{ mr: 1, color: 'text.secondary' }} />
                  ),
                }}
              />

              <TextField
                fullWidth
                select
                label="Company Size"
                name="company_size"
                value={preferences.company_size}
                onChange={handleInputChange}
                required
                sx={{ mb: 3 }}
              >
                {companySizes.map((option) => (
                  <MenuItem key={option.value} value={option.value}>
                    {option.label}
                  </MenuItem>
                ))}
              </TextField>

              <TextField
                fullWidth
                label="Role Type"
                name="role_type"
                value={preferences.role_type}
                onChange={handleInputChange}
                required
                sx={{ mb: 3 }}
                placeholder="e.g., Software Engineer, Data Scientist"
              />

              <TextField
                fullWidth
                label="Additional Information"
                name="additional_info"
                value={preferences.additional_info}
                onChange={handleInputChange}
                multiline
                rows={4}
                sx={{ mb: 3 }}
                placeholder="Any specific requirements or preferences..."
              />

              <Button
                type="submit"
                variant="contained"
                size="large"
                fullWidth
                disabled={isLoading}
                sx={{ mt: 2 }}
              >
                {isLoading ? (
                  <Box sx={{ display: 'flex', alignItems: 'center' }}>
                    <CircularProgress size={24} sx={{ mr: 1 }} />
                    Starting Search...
                  </Box>
                ) : (
                  'Start Job Search'
                )}
              </Button>
            </Box>
          </Paper>
        </Box>
      </Container>
    </ThemeProvider>
  );
}
