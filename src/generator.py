def generate_response(
    persona,
    user_query,
    retrieved_docs
):

    context = "\n\n".join(
        [
            doc["content"]
            for doc in retrieved_docs
        ]
    )

    if persona == "Technical Expert":

        response = f"""
Technical Analysis

Based on the support documentation:

{context[:600]}

Suggested Troubleshooting:

1. Review system configuration
2. Verify credentials
3. Follow documented steps
4. Check logs for errors
"""

    elif persona == "Frustrated User":

        response = f"""
I understand how frustrating this can be.

Based on our support documentation:

{context[:600]}

Please try the recommended steps above.

If the issue continues, we can escalate it for further investigation.
"""

    else:

        response = f"""
Business Summary

Operational Impact:
The issue may affect service availability and business operations.

Recommended Action:
Review the incident status updates and monitor restoration progress.

Relevant Guidance:
{context[:500]}

Please follow the documented guidance.
"""

    return response