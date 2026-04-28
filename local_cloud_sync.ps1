# local_cloud_sync.ps1
Write-Host "🚀 Local Cloud Sync is ACTIVE." -ForegroundColor Cyan
Write-Host "Ready to sync your GitHub changes to Kubernetes." -ForegroundColor Yellow

while($true) {
    Write-Host ""
    $input = Read-Host "Press ENTER to Sync your Local Cloud with GitHub"
    
    Write-Host "🔄 Syncing with GitHub..." -ForegroundColor Green
    kubectl rollout restart deployment/smp-web
    
    Write-Host "✅ Update triggered! Refresh your browser in 10 seconds." -ForegroundColor Cyan
    Write-Host "--------------------------------------------------"
}
