param([int[]]$SlidesToRender = @())
$ErrorActionPreference = 'Stop'
$taskRoot = 'C:\Files\Shared\Online Class\ITM\Sem7\FYP\fyp-research'
$taskDeckPath = Join-Path $taskRoot 'output\presentations\Road-Damage-Proposal.pptx'
$taskPdfPath = Join-Path $taskRoot 'output\presentations\Road-Damage-Proposal.pdf'
$taskRenders = Join-Path $taskRoot 'tmp\slides-road-damage\rendered'
New-Item -ItemType Directory -Path $taskRenders -Force | Out-Null
$taskPpt = New-Object -ComObject PowerPoint.Application
$taskPresentation = $null
try {
    $taskPresentation = $taskPpt.Presentations.Open($taskDeckPath, -1, 0, 0)
    $taskIssues = @()
    foreach ($taskSlide in $taskPresentation.Slides) {
        if ($SlidesToRender.Count -gt 0 -and $taskSlide.SlideIndex -notin $SlidesToRender) { continue }
        $taskSlide.Export((Join-Path $taskRenders ('slide-{0:D2}.png' -f $taskSlide.SlideIndex)), 'PNG', 1920, 1080)
        foreach ($taskShape in $taskSlide.Shapes) {
            if ($taskShape.HasTextFrame -and $taskShape.TextFrame.HasText) {
                $taskBoundHeight = $taskShape.TextFrame.TextRange.BoundHeight
                $taskBoundWidth = $taskShape.TextFrame.TextRange.BoundWidth
                if ($taskBoundHeight -gt $taskShape.Height + 3 -or $taskBoundWidth -gt $taskShape.Width + 3) {
                    $taskIssues += [pscustomobject]@{Slide=$taskSlide.SlideIndex;Text=$taskShape.TextFrame.TextRange.Text;BoxHeight=$taskShape.Height;BoundHeight=$taskBoundHeight;BoxWidth=$taskShape.Width;BoundWidth=$taskBoundWidth}
                }
            }
        }
    }
    $taskPresentation.SaveAs($taskPdfPath, 32)
    $taskIssues | ConvertTo-Json -Depth 3 | Set-Content -LiteralPath (Join-Path $taskRoot 'tmp\slides-road-damage\text-fit.json') -Encoding UTF8
    Write-Output ('Rendered {0} slides in PowerPoint; text-fit flags: {1}' -f $taskPresentation.Slides.Count,$taskIssues.Count)
    $taskIssues | Format-Table -AutoSize
} finally {
    if ($null -ne $taskPresentation) {$taskPresentation.Close()}
    $taskPpt.Quit()
    [System.Runtime.InteropServices.Marshal]::ReleaseComObject($taskPpt) | Out-Null
}
