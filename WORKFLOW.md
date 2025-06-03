 ## Branching Strategy
 - **main**: Production-ready code, merged after PR reviews.
 - **feature/***: For new features (e.g., `feature/helm-chart`, `feature/ci-cd`).
 - **bugfix/***: For bug fixes (e.g., `bugfix/fix-deployment`).

 ## Workflow
 1. **Create a Feature Branch**:
    ```bash
    git checkout -b feature/<feature-name>
    git add .
    git commit -m "feat: <description>"
    git push origin feature/<feature-name>
    ```
 2. **Open a Pull Request**:
    - Create a PR on GitHub from `feature/<feature-name>` to `main`.
    - Include a detailed description and request a review.
 3. **Resolve Conflicts**:
    - If conflicts occur, resolve them locally:
      ```bash
      git checkout main
      git pull origin main
      git checkout feature/<feature-name>
      git merge main
      # Resolve conflicts in editor
      git add .
      git commit
      git push origin feature/<feature-name>
      ```
    - Or use GitHub’s web editor to resolve conflicts.
 4. **Merge PR**:
    - After review, merge the PR into `main` and delete the feature branch.

 ## Commit Steps
 - Use semantic messages:
   - `feat`: New feature (e.g., `feat: add Helm chart`).
   - `fix`: Bug fix (e.g., `fix: resolve YAML parse error`).
   - `chore`: Maintenance tasks (e.g., `chore: update Dockerfile`).
   - `docs`: Documentation tasks (e.g., `docs: add workflow documentation`).