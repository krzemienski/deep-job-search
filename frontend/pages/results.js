import { useState, useEffect } from 'react'
import { useRouter } from 'next/router'
import Head from 'next/head'
import Link from 'next/link'

export default function Results() {
  const router = useRouter()
  const [taskId, setTaskId] = useState(null)
  const [taskStatus, setTaskStatus] = useState(null)
  const [jobListings, setJobListings] = useState([])
  const [followUpQuestions, setFollowUpQuestions] = useState([])
  const [error, setError] = useState(null)
  const [progress, setProgress] = useState(0)

  useEffect(() => {
    const storedTaskId = sessionStorage.getItem('taskId')
    if (!storedTaskId) {
      router.replace('/resume-upload')
      return
    }
    setTaskId(storedTaskId)
  }, [router])

  useEffect(() => {
    let pollInterval

    const pollTaskStatus = async () => {
      if (!taskId) return

      try {
        const response = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/api/task/${taskId}`)
        if (!response.ok) throw new Error('Failed to fetch task status')

        const data = await response.json()
        setTaskStatus(data.status)
        setProgress(data.progress || 0)

        if (data.result) {
          if (data.result.current_jobs) {
            setJobListings(data.result.current_jobs)
          }
          if (data.result.followup_questions) {
            setFollowUpQuestions(data.result.followup_questions)
          }
        }

        if (data.error) {
          setError(data.error)
          clearInterval(pollInterval)
        }

        // Stop polling if task is complete
        if (['SUCCESS', 'FAILURE'].includes(data.status)) {
          clearInterval(pollInterval)
        }
      } catch (err) {
        setError(err.message)
        clearInterval(pollInterval)
      }
    }

    if (taskId) {
      pollTaskStatus() // Initial poll
      pollInterval = setInterval(pollTaskStatus, 5000) // Poll every 5 seconds
    }

    return () => {
      if (pollInterval) clearInterval(pollInterval)
    }
  }, [taskId])

  if (error) {
    return (
      <div className="min-h-screen bg-gray-50 flex items-center justify-center">
        <div className="text-center">
          <div className="text-red-600 text-xl">Error: {error}</div>
          <Link href="/preferences"
            className="mt-4 inline-flex items-center px-4 py-2 border border-transparent text-base font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700">
            Try Again
          </Link>
        </div>
      </div>
    )
  }

  if (!taskStatus || ['PENDING', 'STARTED', 'PROGRESS'].includes(taskStatus)) {
    return (
      <div className="min-h-screen bg-gray-50 flex items-center justify-center">
        <div className="text-center">
          <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-indigo-600 mx-auto"></div>
          <p className="mt-4 text-gray-600">Searching for job matches... ({progress}%)</p>
          {jobListings.length > 0 && (
            <p className="mt-2 text-sm text-gray-500">Found {jobListings.length} matches so far</p>
          )}
        </div>
      </div>
    )
  }

  return (
    <div className="min-h-screen bg-gray-50 py-12 px-4 sm:px-6 lg:px-8">
      <Head>
        <title>Job Matches - Deep Job Search</title>
      </Head>

      <div className="max-w-7xl mx-auto">
        <div className="text-center">
          <h2 className="mt-6 text-3xl font-extrabold text-gray-900">
            Your Job Matches
          </h2>
          <p className="mt-2 text-sm text-gray-600">
            We found {jobListings.length} jobs that match your profile and preferences
          </p>
        </div>

        {followUpQuestions.length > 0 && (
          <div className="mt-8 bg-white shadow sm:rounded-lg">
            <div className="px-4 py-5 sm:p-6">
              <h3 className="text-lg leading-6 font-medium text-gray-900">
                Follow-up Questions
              </h3>
              <div className="mt-2 max-w-xl text-sm text-gray-500">
                <p>Consider these questions to refine your search:</p>
              </div>
              <div className="mt-4 space-y-2">
                {followUpQuestions.map((question, index) => (
                  <div key={index} className="flex items-start">
                    <span className="flex-shrink-0 text-indigo-600">•</span>
                    <p className="ml-2 text-gray-700">{question}</p>
                  </div>
                ))}
              </div>
            </div>
          </div>
        )}

        <div className="mt-12 grid gap-6 lg:grid-cols-2">
          {jobListings.map((job, index) => (
            <div
              key={index}
              className="bg-white shadow rounded-lg p-6 hover:shadow-lg transition-shadow duration-200"
            >
              <div className="flex justify-between items-start">
                <div>
                  <h3 className="text-lg font-medium text-gray-900">
                    {job.title}
                  </h3>
                  <p className="mt-1 text-sm text-gray-500">
                    {job.company}
                  </p>
                </div>
                <span className="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-green-100 text-green-800">
                  {job.location}
                </span>
              </div>

              <p className="mt-4 text-sm text-gray-600 line-clamp-3">
                {job.description}
              </p>

              <div className="mt-6 flex justify-between items-center">
                <a
                  href={job.apply_link}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md shadow-sm text-white bg-indigo-600 hover:bg-indigo-700"
                >
                  Apply Now
                </a>

                <button
                  onClick={() => window.open(job.apply_link, '_blank')}
                  className="text-sm text-gray-500 hover:text-gray-700"
                >
                  View Details
                </button>
              </div>
            </div>
          ))}
        </div>

        <div className="mt-12 text-center space-x-4">
          <Link href="/preferences"
            className="inline-flex items-center px-4 py-2 border border-gray-300 shadow-sm text-sm font-medium rounded-md text-gray-700 bg-white hover:bg-gray-50">
            Refine Search
          </Link>
          <a
            href={`${process.env.NEXT_PUBLIC_API_URL}:5555`}
            target="_blank"
            rel="noopener noreferrer"
            className="inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700"
          >
            View Task Status
          </a>
        </div>
      </div>
    </div>
  )
}
