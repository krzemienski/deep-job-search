import { useRouter } from 'next/router';
import Head from 'next/head';
import { 
  Container, 
  Typography, 
  Button, 
  Box, 
  Paper, 
  Grid, 
  Card, 
  CardContent, 
  CardActions, 
  createTheme, 
  ThemeProvider 
} from '@mui/material';
import { 
  WorkOutline, 
  CloudUpload, 
  Search, 
  TrendingUp 
} from '@mui/icons-material';

const theme = createTheme({
  palette: {
    mode: 'dark',
  },
});

export default function Home() {
  const router = useRouter();

  return (
    <ThemeProvider theme={theme}>
      <Head>
        <title>Deep Job Search - AI-Powered Job Matching</title>
        <meta name="description" content="Find your perfect job match with AI" />
      </Head>

      <Container maxWidth="lg">
        <Box sx={{ my: 4 }}>
          <Typography
            variant="h2"
            component="h1"
            gutterBottom
            align="center"
            sx={{ fontWeight: 'bold', mb: 4 }}
          >
            Deep Job Search
          </Typography>

          <Typography
            variant="h5"
            align="center"
            color="textSecondary"
            paragraph
            sx={{ mb: 6 }}
          >
            Leverage AI to find your perfect job match. Upload your resume and let our
            advanced algorithms do the work.
          </Typography>

          <Box sx={{ display: 'flex', justifyContent: 'center', mb: 8 }}>
            <Button
              variant="contained"
              size="large"
              onClick={() => router.push('/resume-upload')}
              startIcon={<CloudUpload />}
              sx={{ mr: 2 }}
            >
              Upload Resume
            </Button>
          </Box>

          <Grid container spacing={4}>
            <Grid item xs={12} md={4}>
              <Card sx={{ height: '100%' }}>
                <CardContent>
                  <Box sx={{ textAlign: 'center', mb: 2 }}>
                    <CloudUpload sx={{ fontSize: 40, color: 'primary.main' }} />
                  </Box>
                  <Typography variant="h6" component="h2" gutterBottom align="center">
                    Upload Resume
                  </Typography>
                  <Typography color="textSecondary" align="center">
                    Upload your resume in PDF or image format. Our AI will analyze your
                    experience and skills.
                  </Typography>
                </CardContent>
              </Card>
            </Grid>

            <Grid item xs={12} md={4}>
              <Card sx={{ height: '100%' }}>
                <CardContent>
                  <Box sx={{ textAlign: 'center', mb: 2 }}>
                    <Search sx={{ fontSize: 40, color: 'primary.main' }} />
                  </Box>
                  <Typography variant="h6" component="h2" gutterBottom align="center">
                    AI-Powered Search
                  </Typography>
                  <Typography color="textSecondary" align="center">
                    Our advanced AI algorithms analyze job listings to find the best
                    matches for your profile.
                  </Typography>
                </CardContent>
              </Card>
            </Grid>

            <Grid item xs={12} md={4}>
              <Card sx={{ height: '100%' }}>
                <CardContent>
                  <Box sx={{ textAlign: 'center', mb: 2 }}>
                    <TrendingUp sx={{ fontSize: 40, color: 'primary.main' }} />
                  </Box>
                  <Typography variant="h6" component="h2" gutterBottom align="center">
                    Smart Recommendations
                  </Typography>
                  <Typography color="textSecondary" align="center">
                    Get personalized job recommendations that improve over time based on
                    your preferences.
                  </Typography>
                </CardContent>
              </Card>
            </Grid>
          </Grid>

          <Paper sx={{ mt: 8, p: 4 }}>
            <Typography variant="h5" component="h3" gutterBottom align="center">
              Why Choose Deep Job Search?
            </Typography>
            <Grid container spacing={3} sx={{ mt: 2 }}>
              <Grid item xs={12} sm={6}>
                <Box sx={{ display: 'flex', alignItems: 'center', mb: 2 }}>
                  <WorkOutline sx={{ mr: 2, color: 'primary.main' }} />
                  <Typography variant="body1">AI-Powered Job Matching</Typography>
                </Box>
                <Box sx={{ display: 'flex', alignItems: 'center', mb: 2 }}>
                  <WorkOutline sx={{ mr: 2, color: 'primary.main' }} />
                  <Typography variant="body1">Smart Resume Analysis</Typography>
                </Box>
              </Grid>
              <Grid item xs={12} sm={6}>
                <Box sx={{ display: 'flex', alignItems: 'center', mb: 2 }}>
                  <WorkOutline sx={{ mr: 2, color: 'primary.main' }} />
                  <Typography variant="body1">Real-time Updates</Typography>
                </Box>
                <Box sx={{ display: 'flex', alignItems: 'center', mb: 2 }}>
                  <WorkOutline sx={{ mr: 2, color: 'primary.main' }} />
                  <Typography variant="body1">Personalized Recommendations</Typography>
                </Box>
              </Grid>
            </Grid>
          </Paper>
        </Box>
      </Container>
    </ThemeProvider>
  );
}
