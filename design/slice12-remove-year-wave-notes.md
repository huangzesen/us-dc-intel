# Slice 12: Remove Year Wave Chart

The year-based "Project signals by year, 2018-2030" chart was removed from section 03 because the `year` field is mostly NULL across the facility registry and fully NULL for non-US facilities, making the visualization misleading outside the US scope.

The status-based COMPUTE HORIZON card remains in section 03 as the replacement. It uses project status / commitment phase rather than year, so it continues to render globally and keeps the interactive phase toggles intact.
